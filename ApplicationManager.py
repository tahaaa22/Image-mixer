from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt
import logging, time
from ImageClass import *


# Standard Logging Levels:

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename="results.log", level=logging.INFO, format='%(asctime)s - %(message)s')

class WorkerThread(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        # Perform your time-consuming operation here
        for i in range(1, 6):
            self.msleep(2000)  # Simulating a time-consuming operation
            if self.isInterruptionRequested():
                print("Thread interrupted. Aborted.")
                return

            print(f"Task {i} completed")
        self.finished_signal.emit()

class AppManager:
    def __init__(self, ui):
        self.UI = ui
        self.RawImageViews = [ui.Image_1, ui.Image_2, ui.Image_3, ui.Image_4]
        self.ComponentImageViews = [ui.Image1_component, ui.Image2_component, ui.Image3_component, ui.Image4_component]
        self.Images = {
            0: None,
            1: None,
            2: None,
            3: None
        }
        # The list below is not list of image views, but rather 1.components displayed, 2.slider_value, 3.index of combobox
        self.ComponentImages = [[None, 0, 0], [None, 0, 0], [None, 0, 0], [None, 0, 0]]
        self.reconstructed_image_uint8 = None
        self.timer = None
        self.start_time = None
        self.end_time = None
        self.first_press_x_coordinates = 0
        self.first_press_y_coordinates = 0
        self.mixing_type_comboBox_previous_index = 0
        self.components_comboBoxes = [self.UI.Image1_component_comboBox, self.UI.Image2_component_comboBox,
                                      self.UI.Image3_component_comboBox, self.UI.Image4_component_comboBox]

    def load_image(self, image_view):
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
            file_path, _ = file_dialog.getOpenFileName()

            if file_path:
                image_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(image_array, (200, 200))

                image_object = OurImage(resized_image)
                self.Images[int(image_view.objectName()[-1]) - 1] = image_object
                self.display_image(image_view, resized_image)
                self.view_component(int(image_view.objectName()[-1]) - 1, 0)

    @staticmethod
    def display_image(image_view, image_array):
            transposed_array = np.transpose(image_array)
            image_view.clear()
            image_view.setImage(transposed_array)

    def view_component(self, image_view_index, component_index):
        if self.Images[image_view_index]:
            if component_index == 0:
                self.display_image(self.ComponentImageViews[image_view_index],
                                   self.Images[image_view_index].viewed_magnitude)
            else:
                self.display_image(self.ComponentImageViews[image_view_index],
                                   self.Images[image_view_index].Components[component_index])
            self.ComponentImages[image_view_index][0] = self.Images[image_view_index].Components[component_index]
            self.ComponentImages[image_view_index][2] = component_index
            index_to_component = ["Magnitude", "Phase", "Real Part", "Imaginary Part"]
            logging.info(f"Image View {image_view_index + 1} switched to component {index_to_component[component_index]}.")

    def update_slider_values(self):
        sliders = [self.UI.image1_component1_slider, self.UI.image2_component1_slider, self.UI.image3_component1_slider, self.UI.image4_component1_slider]
        for i in range(4):
            self.ComponentImages[i][1] = sliders[i].value()

    def run_function(self):
        # Create and start the worker thread
        self.worker_thread = WorkerThread()
        self.worker_thread.finished_signal.connect(self.function_finished)
        self.worker_thread.start()

    @staticmethod
    def function_finished():
        print("Synchronous Function completed")

    def abort(self):
        if hasattr(self, 'worker_thread') and self.worker_thread.isRunning():
            print("Aborting...")
            self.worker_thread.requestInterruption()

    def mix(self):
        self.UI.open_window()
        self.start_progress()
        self.run_function()
        self.start_time = time.time()
        if self.UI.component_radioButton.isChecked():
            image = self.component_mix()
        else:
            image = self.region_mix()
        if self.UI.output1_button.isChecked():
            self.display_image(self.UI.ui.output_1, image)
        else:
            self.display_image(self.UI.ui.output_2, image)

    def component_mix(self):
        self.update_slider_values()
        # 1. Magnitude 2. Phase 3. Real 4. Imaginary
        output_components = [0, 0, 0, 0]
        for component_value, slider_value, component_type in self.ComponentImages:
            if component_value is None:
                continue
            output_components[component_type] += component_value * slider_value / 100.0

        self.end_time = time.time()
        logging.info(f"Components Mixing Done in {self.end_time - self.start_time} second(s)")
        return self.reconstruct_image(output_components)

    def region_mix(self):
        slider_value = self.UI.RegionSlider.value()
    
        output_components = [0, 0, 0, 0]
        for component_data, _, component_index in self.ComponentImages:
            if component_data is None:
                continue
            image_array = component_data.copy()
            if self.UI.OuterButton.isChecked():
                image_array[100 - slider_value : 100 + slider_value , 100 - slider_value: 100 + slider_value] = 0
            else:
                image_array[:100 - slider_value, :] = 0
                image_array[100 + slider_value:, :] = 0
                image_array[:, :100 - slider_value] = 0
                image_array[:, 100 + slider_value:] = 0

            output_components[component_index] += image_array

        self.end_time = time.time()
        logging.info(f"Region Mixing Done in {self.end_time - self.start_time} second(s)")
        return self.reconstruct_image(output_components)

    def start_progress(self):
        self.UI.ui.progressBar.setValue(0)
        interval = 40 # milliseconds

        # Create a timer to update the progress
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(interval)

    def update_progress(self):
        # Increment the progress bar value
        current_value = self.UI.ui.progressBar.value()
        new_value = min(current_value + int(100 / (1000 / 40)), 100)
        self.UI.ui.progressBar.setValue(new_value)
        # Stop the timer when the progress reaches 100%
        if new_value == 100:
            self.timer.stop()

    def reconstruct_image(self, output_components):
        output_mag_phase = (output_components[0]) * np.exp(1j * output_components[1])
        output_real_imag = output_components[2] + 1j * output_components[3]
        output_combined_components = output_mag_phase + output_real_imag
        
        # Perform the Inverse Fourier Transform to reconstruct the image
        reconstructed_image = np.fft.ifft2(np.fft.ifftshift(output_combined_components)).real
        # Normalize the pixel values to the range [0, 255] for display
        reconstructed_image_normalized = cv2.normalize(reconstructed_image, None, 0, 255, cv2.NORM_MINMAX)
        # Convert to uint8 for display (grayscale image)
        self.reconstructed_image_uint8 = np.uint8(reconstructed_image_normalized)
        return self.reconstructed_image_uint8

    def calculate_changes_percentages(self, image_view, image_view_index, new_x_coordinates, new_y_coordinates):
        if image_view in self.RawImageViews:
            if image_view.getImageItem:
                x_change_percentage = float((new_x_coordinates - self.first_press_x_coordinates) / self.first_press_x_coordinates)
                y_change_percentage = float((self.first_press_y_coordinates - new_y_coordinates) / new_y_coordinates)
                if (x_change_percentage < -0.01 or x_change_percentage > 0.01) and (-0.2 <= y_change_percentage <= 0.2):
                    if x_change_percentage > 3.0:
                        x_change_percentage = 3.0
                    elif x_change_percentage < -1.0:
                        x_change_percentage = -1.0
                    x_change_percentage += 1.0
                    self.change_contrast(image_view, image_view_index, x_change_percentage)
                elif (y_change_percentage < -0.01 or y_change_percentage > 0.01) and (-0.2 <= x_change_percentage <= 0.2):
                    if y_change_percentage > 3.0:
                        y_change_percentage = 3.0
                    elif y_change_percentage < -3.0:
                        y_change_percentage = -3.0
                    y_change_percentage = (y_change_percentage / 3.0) * 100
                    if y_change_percentage > 0:
                        y_change_percentage += 30
                    else:
                        y_change_percentage -= 30
                    self.change_brightness(image_view, image_view_index, y_change_percentage)


    def change_brightness(self, image_view,image_view_index, beta):
        if self.Images[image_view_index]:
            raw_image = self.Images[image_view_index].image_data
            adjusted_image = cv2.convertScaleAbs(raw_image, None, 1.0, beta)
            self.display_image(image_view, adjusted_image)

    def change_contrast(self, image_view, image_view_index, alpha):
        if self.Images[image_view_index]:
            raw_image = self.Images[image_view_index].image_data
            adjusted_image = cv2.convertScaleAbs(raw_image, None, alpha, 0.0)
            self.display_image(image_view, adjusted_image)


    def draw_region(self):
        slider_value = self.UI.RegionSlider.value()
        start_point = (100 - slider_value,  100 - slider_value)
        end_point = (100 + slider_value,100 + slider_value)
        color = (255, 0, 0)

        if self.UI.region_button.isChecked():
            for i in range(4):
                if self.Images[i]:
                    data = self.Images[i].image_data.copy()
                    image = cv2.rectangle(data, start_point, end_point, color, 2)
                    self.display_image(self.RawImageViews[i], image)

    def reset_brightness_and_contrast(self):
        for i in range(len(self.Images)):
            if self.Images[i]:
                self.display_image(self.RawImageViews[i], self.Images[i].image_data)


    def hide_components(self):
        comboboxes_mag_phas_components = ["FT Magnitude", "FT Phase", "", ""]
        comboboxes_real_imag_components = ["", "", "FT Real", "FT Imaginary"]
        comboboxes_all_components = ["FT Magnitude", "FT Phase", "FT Real", "FT Imaginary"]
        if self.UI.mixing_type_comboBox.currentIndex() == 0:
            for i in range(4):
                self.components_comboBoxes[i].clear()
                self.components_comboBoxes[i].insertItems(0, comboboxes_all_components)
        elif self.UI.mixing_type_comboBox.currentIndex() == 1:
            for i in range(4):
                self.components_comboBoxes[i].clear()
                self.components_comboBoxes[i].insertItems(0, comboboxes_mag_phas_components)
        elif self.UI.mixing_type_comboBox.currentIndex() == 2:
            for i in range(4):
                self.components_comboBoxes[i].clear()
                self.components_comboBoxes[i].insertItems(2, comboboxes_real_imag_components)
                self.components_comboBoxes[i].setCurrentIndex(2)
                self.display_image(self.ComponentImageViews[i], self.Images[i].Components[2])

