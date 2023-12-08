from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QObject, QEvent

class EventFilter(QObject):
    def eventFilter(self, watched, event):
        if event.type() == QEvent.MouseButtonDblClick:
            self.File_Path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        return super().eventFilter(watched, event)
class ApplicationManager:

    def __init__(self, Ui):
        self.UI = Ui


    def Browse_Signal(self):
        # self.clear_graphs()
        self.File_Path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        # if self.File_Path:


