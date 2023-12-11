from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import cv2
from ImageClass import *

class AppManager:
    def __init__(self,ui):
        self.UI = ui
        self.RawImageViews = [ui.Image_1,ui.Image_2,ui.Image_3,ui.Image_4]
        self.ComponentImageViews = [ui.Image1_component,ui.Image2_component,ui.Image3_component,ui.Image4_component]
        self.Images = []

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
    






