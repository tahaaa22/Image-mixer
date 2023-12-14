from PyQt5.QtWidgets import QFileDialog
from ImageClass import *
from pyqtgraph import RectROI,ROI
import cv2
from PyQt5.QtCore import QTimer, QThread, pyqtSignal

class WorkerThread(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        # Perform your time-consuming operation here
        for i in range(1, 6):
            self.msleep(2000)  # Simulating a time-consuming operation
            if self.isInterruptionRequested():
                print("Thread interrupted. Aborting...")
                return

            print(f"Task {i} completed")
        self.finished_signal.emit()

class AppManager:
    def __init__(self, ui):
        self.UI = ui
        self.RawImageViews = [ui.Image_1,ui.Image_2,ui.Image_3,ui.Image_4]
        self.ComponentImageViews = [ui.Image1_component,ui.Image2_component,ui.Image3_component,ui.Image4_component]
        self.Images = []
        # The list below is not list of image views, but rather 1.components displayed, 2.slider_value, 3.index of combobox
        self.ComponentImages = [[None, 0, 0], [None, 0, 0], [None, 0, 0], [None, 0, 0]]
        self.reconstructed_image_uint8 = None
        self.timer = None
        #self.roi = RectROI((0,0), (0,0), centered=True)


    def load_image(self, image_view):
        if image_view in self.RawImageViews:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
            file_path, _ = file_dialog.getOpenFileName()

            if file_path:
                image_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(image_array, (200,200))

                image_object = OurImage(resized_image)
                self.Images.append(image_object)

                self.display_image(image_view,resized_image)
                self.view_component(int(image_view.objectName()[-1]) - 1, 0)

    @staticmethod
    def display_image(image_view, image_array):
        transposed_array = np.transpose(image_array)
        image_view.clear()
        image_view.setImage(transposed_array)

    def view_component(self, image_view_index, component_index):
        self.ComponentImageViews[image_view_index].setImage(self.Images[image_view_index].Components[component_index])
        self.ComponentImages[image_view_index][0] = self.Images[image_view_index].Components[component_index]
        self.ComponentImages[image_view_index][2] = component_index

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
        output_components = [1, 0, 0, 0]
        for component_value, slider_value, component_type in self.ComponentImages:
            if component_value is None:
                continue
            output_components[component_type] += component_value * slider_value / 100.0
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

    def region_mix(self):

        slider_value = self.UI.RegionSlider.value()
        # for i in range(4):
        #     self.roi.setPos(100 - slider_value,100 - slider_value)
        #     self.roi.setSize((slider_value, slider_value))
        #     self.roi.setPen(255,255,255,255)
        #     self.ComponentImageViews[i].addItem(self.roi)
        
        output_components = [1, 0, 0, 0]
        for component_data, _, component_index in self.ComponentImages:
            if component_data is None:
                continue
            image_array = component_data
            if self.UI.OuterButton.isChecked():
                image_array[100 - slider_value : 100 + slider_value , 100 - slider_value: 100 + slider_value] = 0
            else:
                image_array[:100 - slider_value, :] = 0
                image_array[100 + slider_value:, :] = 0
                image_array[:, :100 - slider_value] = 0
                image_array[:, 100 + slider_value:] = 0

            output_components[component_index] += image_array
        return self.reconstruct_image(output_components)
        
    def reconstruct_image(self, output_components):
        output_mag_phase = output_components[0] * np.exp(1j * output_components[1])
        output_real_imag = output_components[2] + 1j * output_components[3]
        output_combined_components = output_mag_phase + output_real_imag
        
        # Perform the Inverse Fourier Transform to reconstruct the image
        reconstructed_image = np.fft.ifft2(np.fft.ifftshift(output_combined_components)).real
        # Normalize the pixel values to the range [0, 255] for display
        reconstructed_image_normalized = cv2.normalize(reconstructed_image, None, 0, 255, cv2.NORM_MINMAX)
        # Convert to uint8 for display (grayscale image)
        self.reconstructed_image_uint8 = np.uint8(reconstructed_image_normalized)
        return self.reconstructed_image_uint8
        

        
        

        
        

    

