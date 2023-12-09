from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QEvent
from PIL import Image
import cv2
import numpy as np

Displayed_Images = {
    "image_1" : None,
    "image_2" : None,
    "image_3" : None,
    "image_4" : None
}


def display_components(input_label,index,output_label):
    
    image_array = cv2.imread(Displayed_Images[input_label.objectName()], cv2.IMREAD_GRAYSCALE)
    
    f_transform = np.fft.fft(image_array)
    f_transform_shifted = np.fft.fftshift(f_transform)

    if index == 0:
        component = np.abs(f_transform_shifted)
    if index == 1:
        component = np.angle(f_transform_shifted)
    if index == 2:
        component = np.real(f_transform_shifted)
    if index == 3:
        component = np.imag(f_transform_shifted)

    url = array_to_pixmap(component)
    output_label.setPixmap(QtGui.QPixmap(url))


def array_to_pixmap(array):
    array = array.astype(np.uint8)
    component_image = Image.fromarray(array)
    component_image.save("output.png")
    return "output.png"

    



class QLabel(QtWidgets.QLabel):
    image_index = 0
    def __init__(self):
        super().__init__()
        self.Image_Path = None
        self.Image = None
        

    def mouseDoubleClickEvent(self, event):
        if event.type() == QEvent.MouseButtonDblClick:
            self.Image_Path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        if self.Image_Path:
            self.Image = Image.open(self.Image_Path).convert('L')
            self.Image.save(f'greyscale{QLabel.image_index}.png')
            self.setPixmap(QtGui.QPixmap(f"greyscale{QLabel.image_index}.png"))
            Displayed_Images[self.objectName()] = f"greyscale{QLabel.image_index}.png"
            QLabel.image_index+=1



