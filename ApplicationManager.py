from PyQt5.QtWidgets import QFileDialog
from PIL import Image
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
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_path, _ = file_dialog.getOpenFileName()

        if file_path:
            img = Image.open(file_path)
            # gray_img = img.convert("L")
            # image_array = np.array(gray_img)
            image_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            
            image_object = OurImage(image_array)
            self.Images.append(image_object)

            image_view.setImage(image_array)
            self.view_component(int(image_view.objectName()[-1]) - 1, 0)

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
            # Just to test, I display on image 4
            self.RawImageViews[3].setImage(self.reconstructed_image_uint8)
        else:
            pass




