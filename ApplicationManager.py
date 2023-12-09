from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QEvent
from PIL import Image

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






