from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QEvent
from PIL import Image
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np

class QLabel(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.Image_Path = None
        self.Image = None
    def mouseDoubleClickEvent(self, event):
        if event.type() == QEvent.MouseButtonDblClick:
            self.Image_Path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        if self.Image_Path:
            self.Image = Image.open(self.Image_Path).convert('L')
            self.Image.save('greyscale.png')
            self.setPixmap(QtGui.QPixmap("greyscale.png"))


class ApplicationManager:
    def __init__(self, ui, images):
        self.UI = ui
        self.Images = images   



def display_components(image_path,index,label):
    
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    f_transform = np.fft.fft(original_image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    if index == 0:
        component = np.abs(f_transform_shifted)
    if index == 1:
        component = np.angle(f_transform_shifted)
    if index == 2:
        component = np.real(f_transform_shifted)
    if index == 3:
        component = np.imag(f_transform_shifted)

    pixmap = array_to_pixmap(component)
    label.setPixmap(pixmap)


def array_to_pixmap(array):
    height, width = array.shape
    bytes_per_line = 1 * width
    q_image = QImage(array.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
    pixmap = QPixmap.fromImage(q_image)
    return pixmap

    





