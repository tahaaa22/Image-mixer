from PyQt5.QtWidgets import QFileDialog
from pyqtgraph import RectROI,Color
import cv2
from ImageClass import *

class AppManager:
    def __init__(self, ui):
        self.UI = ui
        self.RawImageViews = [ui.Image_1,ui.Image_2,ui.Image_3,ui.Image_4]
        self.ComponentImageViews = [ui.Image1_component,ui.Image2_component,ui.Image3_component,ui.Image4_component]
        self.Images = []
        # The list below is not list of image views, but rather 1.components displayed, 2.slider_value, 3.index of combobox
        self.ComponentImages = [[None, 0, 0], [None, 0, 0], [None, 0, 0], [None, 0, 0]]
        self.components_mode = True
        self.reconstructed_image_uint8 = None


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

    def display_image(self,image_view,image_array):
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


    def switch_mode(self):
        # TODO Implement this function to switch between the 2 modes
        self.components_mode = not self.components_mode
        # Complete the function.

    def mix(self):
        self.UI.open_window()
        if self.components_mode:
            self.update_slider_values()
            # 1. Magnitude 2. Phase 3. Real 4. Imaginary
            output_components = [1, 0, 0, 0]
            for component_value, slider_value, component_type in self.ComponentImages:
                if component_value is None:
                    continue
                output_components[component_type] += component_value * slider_value / 100.0
            output_mag_phase = output_components[0] * np.exp(1j * output_components[1])
            output_real_imag = output_components[2] + 1j * output_components[3]
            output_combined_components = output_mag_phase + output_real_imag
            # Perform the Inverse Fourier Transform to reconstruct the image
            reconstructed_image = np.fft.ifft2(np.fft.ifftshift(output_combined_components)).real
            # Convert to uint8 for display (grayscale image)
            self.reconstructed_image_uint8 = np.uint8(reconstructed_image)
            if self.UI.output1_button.isChecked():
                self.display_image(self.UI.ui.output_1, self.reconstructed_image_uint8)
            else:
                self.display_image(self.UI.ui.output_2, self.reconstructed_image_uint8)

        else:
            pass


    def region_mix(self):
        pass
        # slider_value = self.UI.RegionSlider.value()
        # for i in range(4):
        #     if self.ComponentImageViews[i] is not None:
        #         if not hasattr(self, 'square_roi'):
        #             self.square_roi = RectROI([50, 50], [slider_value, slider_value])
        #             self.ComponentImageViews[i].addItem(self.square_roi)
        #         else:
        #             self.square_roi.setSize([slider_value, slider_value])

        #         x_position = int(self.square_roi.pos().x())
        #         y_position = int(self.square_roi.pos().y())

        #         roi_image1 = self.Images[i].image_data.copy()
        #         roi_image1[y_position: y_position + slider_value,
        #                 x_position: x_position + slider_value] = 0
        #         self.display_image(self.ComponentImageViews[i], roi_image1)

        # if self.UI.InnerButton.isChecked():
        #     roi_image1 = self.Images[0].image_data[100 - slider_value : 100 + slider_value , 100 - slider_value: 100 + slider_value]
        #     self.display_image(self.RawImageViews[3], roi_image1)
        
        # else:
        #     inner_image = self.Images[0].image_data[100 - slider_value : 100 + slider_value , 100 - slider_value: 100 + slider_value]
        #     roi_image1 = np.setdiff1d(self.Images,inner_image)
        #     self.display_image(self.RawImageViews[2], roi_image1)

