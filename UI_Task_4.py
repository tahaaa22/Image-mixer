from PyQt5 import QtCore, QtGui, QtWidgets
from UI_Output import Ui_Output
from ApplicationManager import *
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.DisplayedImages = []


    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Output()
        self.ui.setupUi(self.window)
        self.window.show()
    def show_RegionBox(self):
        self.RegionBox.setVisible(True)
        self.ComponentMixer.setVisible(False)
        
    def show_ComponentMixer(self):
        self.ComponentMixer.setVisible(True)
        self.RegionBox.setVisible(False)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 857)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #1e1e2f;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)
        self.ImagesBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagesBox.sizePolicy().hasHeightForWidth())
        self.ImagesBox.setSizePolicy(sizePolicy)
        self.ImagesBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border: none;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.ImagesBox.setObjectName("ImagesBox")
        self.gridLayout = QtWidgets.QGridLayout(self.ImagesBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_image1_2 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image1_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1_2.sizePolicy().hasHeightForWidth())
        self.groupBox_image1_2.setSizePolicy(sizePolicy)
        self.groupBox_image1_2.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1_2.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_image1_2.setObjectName("groupBox_image1_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_image1_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.output_imge1_comboBox = QtWidgets.QComboBox(self.groupBox_image1_2)
        self.output_imge1_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.output_imge1_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.output_imge1_comboBox.setObjectName("output_imge1_comboBox")
        self.output_imge1_comboBox.addItem("")
        self.output_imge1_comboBox.addItem("")
        self.gridLayout_6.addWidget(self.output_imge1_comboBox, 0, 0, 1, 1)
        self.component_image1_comboBox = QtWidgets.QComboBox(self.groupBox_image1_2)
        self.component_image1_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.component_image1_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: #1e1e2f;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.component_image1_comboBox.setMaxCount(2147483646)
        self.component_image1_comboBox.setObjectName("component_image1_comboBox")
        self.component_image1_comboBox.addItem("")
        self.component_image1_comboBox.addItem("")
        self.component_image1_comboBox.addItem("")
        self.component_image1_comboBox.addItem("")
        self.gridLayout_6.addWidget(self.component_image1_comboBox, 0, 1, 1, 1)
        self.image_1 = QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_1.sizePolicy().hasHeightForWidth())
        self.image_1.setSizePolicy(sizePolicy)
        self.image_1.setStyleSheet("background-color: #1e1e2f;")
        self.image_1.setText("")
        self.image_1.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.image_1.setScaledContents(True)
        self.image_1.setObjectName("image_1")
        self.DisplayedImages.append(self.image_1)
        self.gridLayout_6.addWidget(self.image_1, 1, 0, 1, 1)
        self.component_image_1 = QtWidgets.QLabel(self.groupBox_image1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.component_image_1.sizePolicy().hasHeightForWidth())
        self.component_image_1.setSizePolicy(sizePolicy)
        self.component_image_1.setStyleSheet("background-color: #1e1e2f;")
        self.component_image_1.setText("")
        self.component_image_1.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.component_image_1.setScaledContents(True)
        self.component_image_1.setObjectName("component_image_1")
        self.gridLayout_6.addWidget(self.component_image_1, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_image1_2)
        self.groupBox_image3 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image3.sizePolicy().hasHeightForWidth())
        self.groupBox_image3.setSizePolicy(sizePolicy)
        self.groupBox_image3.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image3.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_image3.setObjectName("groupBox_image3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_image3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.output_image3_comboBox = QtWidgets.QComboBox(self.groupBox_image3)
        self.output_image3_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.output_image3_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.output_image3_comboBox.setObjectName("output_image3_comboBox")
        self.output_image3_comboBox.addItem("")
        self.output_image3_comboBox.addItem("")
        self.gridLayout_7.addWidget(self.output_image3_comboBox, 0, 0, 1, 1)
        self.component_image3_comboBox = QtWidgets.QComboBox(self.groupBox_image3)
        self.component_image3_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.component_image3_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: #1e1e2f;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.component_image3_comboBox.setMaxCount(2147483646)
        self.component_image3_comboBox.setObjectName("component_image3_comboBox")
        self.component_image3_comboBox.addItem("")
        self.component_image3_comboBox.addItem("")
        self.component_image3_comboBox.addItem("")
        self.component_image3_comboBox.addItem("")
        self.gridLayout_7.addWidget(self.component_image3_comboBox, 0, 1, 1, 1)
        self.image_3 = QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_3.sizePolicy().hasHeightForWidth())
        self.image_3.setSizePolicy(sizePolicy)
        self.image_3.setStyleSheet("background-color: #1e1e2f;")
        self.image_3.setText("")
        self.image_3.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.image_3.setScaledContents(True)
        self.image_3.setObjectName("image_3")
        self.DisplayedImages.append(self.image_3)
        self.gridLayout_7.addWidget(self.image_3, 1, 0, 1, 1)
        self.component_image_3 = QtWidgets.QLabel(self.groupBox_image3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.component_image_3.sizePolicy().hasHeightForWidth())
        self.component_image_3.setSizePolicy(sizePolicy)
        self.component_image_3.setStyleSheet("background-color: #1e1e2f;")
        self.component_image_3.setText("")
        self.component_image_3.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.component_image_3.setScaledContents(True)
        self.component_image_3.setObjectName("component_image_3")
        self.gridLayout_7.addWidget(self.component_image_3, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_image3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_image1 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1.sizePolicy().hasHeightForWidth())
        self.groupBox_image1.setSizePolicy(sizePolicy)
        self.groupBox_image1.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_image1.setObjectName("groupBox_image1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_image1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.output_image2_comboBox = QtWidgets.QComboBox(self.groupBox_image1)
        self.output_image2_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.output_image2_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.output_image2_comboBox.setObjectName("output_image2_comboBox")
        self.output_image2_comboBox.addItem("")
        self.output_image2_comboBox.addItem("")
        self.gridLayout_8.addWidget(self.output_image2_comboBox, 0, 0, 1, 1)
        self.component_image_2_comboBox = QtWidgets.QComboBox(self.groupBox_image1)
        self.component_image_2_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.component_image_2_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: #1e1e2f;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.component_image_2_comboBox.setMaxCount(2147483646)
        self.component_image_2_comboBox.setObjectName("component_image2_comboBox")
        self.component_image_2_comboBox.addItem("")
        self.component_image_2_comboBox.addItem("")
        self.component_image_2_comboBox.addItem("")
        self.component_image_2_comboBox.addItem("")
        self.gridLayout_8.addWidget(self.component_image_2_comboBox, 0, 1, 1, 1)
        self.image_2 = QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_2.sizePolicy().hasHeightForWidth())
        self.image_2.setSizePolicy(sizePolicy)
        self.image_2.setStyleSheet("background-color: #1e1e2f;")
        self.image_2.setText("")
        self.image_2.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.image_2.setScaledContents(True)
        self.image_2.setObjectName("image_2")
        self.DisplayedImages.append(self.image_2)
        self.gridLayout_8.addWidget(self.image_2, 1, 0, 1, 1)
        self.component_image_2 = QtWidgets.QLabel(self.groupBox_image1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.component_image_2.sizePolicy().hasHeightForWidth())
        self.component_image_2.setSizePolicy(sizePolicy)
        self.component_image_2.setStyleSheet("background-color: #1e1e2f;")
        self.component_image_2.setText("")
        self.component_image_2.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.component_image_2.setScaledContents(True)
        self.component_image_2.setObjectName("component_image2")
        self.gridLayout_8.addWidget(self.component_image_2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_image1)
        self.groupBox_image2 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image2.sizePolicy().hasHeightForWidth())
        self.groupBox_image2.setSizePolicy(sizePolicy)
        self.groupBox_image2.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image2.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_image2.setObjectName("groupBox_image2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_image2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.output_image4_comboBox = QtWidgets.QComboBox(self.groupBox_image2)
        self.output_image4_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.output_image4_comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.output_image4_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.output_image4_comboBox.setObjectName("output_image4_comboBox")
        self.output_image4_comboBox.addItem("")
        self.output_image4_comboBox.addItem("")
        self.gridLayout_9.addWidget(self.output_image4_comboBox, 0, 0, 1, 1)
        self.component_image4_comboBox = QtWidgets.QComboBox(self.groupBox_image2)
        self.component_image4_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.component_image4_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: #1e1e2f;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.component_image4_comboBox.setMaxCount(2147483646)
        self.component_image4_comboBox.setObjectName("component_image4_comboBox")
        self.component_image4_comboBox.addItem("")
        self.component_image4_comboBox.addItem("")
        self.component_image4_comboBox.addItem("")
        self.component_image4_comboBox.addItem("")
        self.gridLayout_9.addWidget(self.component_image4_comboBox, 0, 1, 1, 1)
        self.image_4 = QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_4.sizePolicy().hasHeightForWidth())
        self.image_4.setSizePolicy(sizePolicy)
        self.image_4.setStyleSheet("background-color: #1e1e2f;")
        self.image_4.setText("")
        self.image_4.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.image_4.setScaledContents(True)
        self.image_4.setObjectName("image_4")
        self.DisplayedImages.append(self.image_4)
        self.gridLayout_9.addWidget(self.image_4, 1, 0, 1, 1)
        self.companent_image_4 = QtWidgets.QLabel(self.groupBox_image2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companent_image_4.sizePolicy().hasHeightForWidth())
        self.companent_image_4.setSizePolicy(sizePolicy)
        self.companent_image_4.setStyleSheet("background-color: #1e1e2f;")
        self.companent_image_4.setText("")
        self.companent_image_4.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.companent_image_4.setScaledContents(True)
        self.companent_image_4.setObjectName("companent_image_4")
        self.gridLayout_9.addWidget(self.companent_image_4, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_image2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.ImagesBox, 1, 0, 1, 1)
        self.PereferenceBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PereferenceBox.sizePolicy().hasHeightForWidth())
        self.PereferenceBox.setSizePolicy(sizePolicy)
        self.PereferenceBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.PereferenceBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border:none;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.PereferenceBox.setObjectName("PereferenceBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.PereferenceBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.regions_radiobutton = QtWidgets.QRadioButton(self.PereferenceBox)
        self.regions_radiobutton.setObjectName("regions_radiobutton")
        # Connect the radio buttons' clicked signal to the slot
        self.regions_radiobutton.clicked.connect(self.show_RegionBox)
        self.regions_radiobutton.setChecked(True)
        self.gridLayout_4.addWidget(self.regions_radiobutton, 0, 0, 1, 1)
        self.component_radiobutton = QtWidgets.QRadioButton(self.PereferenceBox)
        self.component_radiobutton.setObjectName("component_radiobutton")
        self.component_radiobutton.clicked.connect(self.show_ComponentMixer)
        self.gridLayout_4.addWidget(self.component_radiobutton, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.PereferenceBox, 2, 0, 1, 1)
        self.MIxerbox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MIxerbox.sizePolicy().hasHeightForWidth())
        self.MIxerbox.setSizePolicy(sizePolicy)
        self.MIxerbox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border:none;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.MIxerbox.setObjectName("MIxerbox")
        self.mixer = QtWidgets.QHBoxLayout(self.MIxerbox)
        self.mixer.setObjectName("mixer")
        self.Regionbox = QtWidgets.QVBoxLayout()
        self.Regionbox.setObjectName("Regionbox")
        self.RegionBox = QtWidgets.QGroupBox(self.MIxerbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegionBox.sizePolicy().hasHeightForWidth())
        self.RegionBox.setSizePolicy(sizePolicy)
        self.RegionBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.RegionBox.setTitle("")
        self.RegionBox.setObjectName("RegionBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.RegionBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_16 = QtWidgets.QLabel(self.RegionBox)
        self.label_16.setStyleSheet("background-color: transparent;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_13.addWidget(self.label_16)
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.outer_radiobutton = QtWidgets.QRadioButton(self.RegionBox)
        self.outer_radiobutton.setObjectName("outer_radiobutton")
        self.horizontalLayout_10.addWidget(self.outer_radiobutton)
        self.inner_radiobutton = QtWidgets.QRadioButton(self.RegionBox)
        self.inner_radiobutton.setObjectName("inner_radiobutton")
        self.horizontalLayout_10.addWidget(self.inner_radiobutton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.region_slider = QtWidgets.QSlider(self.RegionBox)
        self.region_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.region_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.region_slider.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background-color: qradialgradient(\n"
"        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
"        radius: 1, stop: 0 #fff, stop: 1 #424242\n"
"        );\n"
"    border-radius: 2px;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }\n"
"\n"
"QSlider::handle::hover{\n"
"    border: inset;\n"
"     background-color: qradialgradient(\n"
"        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
"        radius: 1, stop: 0 #bbb, stop: 1 #000\n"
"        );\n"
"}")
        self.region_slider.setMaximum(100)
        self.region_slider.setProperty("value", 50)
        self.region_slider.setOrientation(QtCore.Qt.Horizontal)
        self.region_slider.setObjectName("region_slider")
        self.horizontalLayout_12.addWidget(self.region_slider)
        self.region_LCD = QtWidgets.QLabel(self.RegionBox)
        self.region_LCD.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.region_LCD.setStyleSheet("background-color: transparent;")
        self.region_LCD.setObjectName("region_LCD")
        self.horizontalLayout_12.addWidget(self.region_LCD)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.apply_region = QtWidgets.QPushButton(self.RegionBox, clicked = lambda: self.open_window())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_region.setFont(font)
        self.apply_region.setObjectName("apply_region")
         # Apply the "btn-success" style to the apply_region button
        self.apply_region.setStyleSheet("""
            QPushButton#apply_region {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            
            QPushButton#apply_region:hover {
                background-color: #218838;
            }
            
            QPushButton#apply_region:pressed {
                background-color: #1e7e34;
            }
        """)

        self.horizontalLayout_11.addWidget(self.apply_region)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.Regionbox.addWidget(self.RegionBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Regionbox.addItem(spacerItem2)
        self.mixer.addLayout(self.Regionbox)
        self.ComponentMixer = QtWidgets.QGroupBox(self.MIxerbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComponentMixer.sizePolicy().hasHeightForWidth())
        self.ComponentMixer.setSizePolicy(sizePolicy)
        self.ComponentMixer.setMaximumSize(QtCore.QSize(803, 809))
        self.ComponentMixer.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.ComponentMixer.setObjectName("ComponentMixer")
        self.ComponentMixer.setVisible(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ComponentMixer)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.ComponentMixer)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border:none;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 39))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: transparent;")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setStyleSheet("background-color: transparent;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.mixer1_image_combobox = QtWidgets.QComboBox(self.groupBox_3)
        self.mixer1_image_combobox.setMinimumSize(QtCore.QSize(0, 22))
        self.mixer1_image_combobox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.mixer1_image_combobox.setObjectName("mixer1_image_combobox")
        self.mixer1_image_combobox.addItem("")
        self.mixer1_image_combobox.addItem("")
        self.mixer1_image_combobox.addItem("")
        self.mixer1_image_combobox.addItem("")
        self.horizontalLayout_3.addWidget(self.mixer1_image_combobox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.component1_slider = QtWidgets.QSlider(self.groupBox_3)
        self.component1_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.component1_slider.setMaximumSize(QtCore.QSize(320, 16777215))
        self.component1_slider.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background-color: qradialgradient(\n"
"        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
"        radius: 1, stop: 0 #fff, stop: 1 #424242\n"
"        );\n"
"    border-radius: 2px;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }\n"
"\n"
"QSlider::handle::hover{\n"
"    border: inset;\n"
"     background-color: qradialgradient(\n"
"        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
"        radius: 1, stop: 0 #bbb, stop: 1 #000\n"
"        );\n"
"}")
        self.component1_slider.setMaximum(100)
        self.component1_slider.setProperty("value", 50)
        self.component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.component1_slider.setObjectName("component1_slider")
        self.horizontalLayout_4.addWidget(self.component1_slider)
        self.mixer1_LCD = QtWidgets.QLabel(self.groupBox_3)
        self.mixer1_LCD.setMaximumSize(QtCore.QSize(16777215, 20))
        self.mixer1_LCD.setStyleSheet("background-color: transparent;")
        self.mixer1_LCD.setObjectName("mixer1_LCD")
        self.horizontalLayout_4.addWidget(self.mixer1_LCD)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.mixer1_component_combobox = QtWidgets.QComboBox(self.groupBox_3)
        self.mixer1_component_combobox.setMinimumSize(QtCore.QSize(0, 22))
        self.mixer1_component_combobox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.mixer1_component_combobox.setObjectName("mixer1_component_combobox")
        self.mixer1_component_combobox.addItem("")
        self.mixer1_component_combobox.addItem("")
        self.mixer1_component_combobox.addItem("")
        self.mixer1_component_combobox.addItem("")
        self.mixer1_component_combobox.addItem("")
        self.mixer1_component_combobox.addItem("")
        self.mixer1_component_combobox.addItem("")
        self.verticalLayout_3.addWidget(self.mixer1_component_combobox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setStyleSheet("background-color: transparent;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.mixer2_image_combobox = QtWidgets.QComboBox(self.groupBox_3)
        self.mixer2_image_combobox.setMinimumSize(QtCore.QSize(0, 22))
        self.mixer2_image_combobox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.mixer2_image_combobox.setObjectName("mixer2_image_combobox")
        self.mixer2_image_combobox.addItem("")
        self.mixer2_image_combobox.addItem("")
        self.mixer2_image_combobox.addItem("")
        self.mixer2_image_combobox.addItem("")
        self.horizontalLayout_5.addWidget(self.mixer2_image_combobox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.component2_slider = QtWidgets.QSlider(self.groupBox_3)
        self.component2_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.component2_slider.setMaximumSize(QtCore.QSize(300, 16777215))
        self.component2_slider.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background-color: qradialgradient(\n"
"        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
"        radius: 1, stop: 0 #fff, stop: 1 #424242\n"
"        );\n"
"    border-radius: 2px;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }\n"
"\n"
"QSlider::handle::hover{\n"
"    border: inset;\n"
"     background-color: qradialgradient(\n"
"        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
"        radius: 1, stop: 0 #bbb, stop: 1 #000\n"
"        );\n"
"}")
        self.component2_slider.setMaximum(100)
        self.component2_slider.setProperty("value", 50)
        self.component2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.component2_slider.setObjectName("component2_slider")
        self.horizontalLayout_8.addWidget(self.component2_slider)
        self.mixer2_LCD = QtWidgets.QLabel(self.groupBox_3)
        self.mixer2_LCD.setMaximumSize(QtCore.QSize(16777215, 20))
        self.mixer2_LCD.setStyleSheet("background-color: transparent;")
        self.mixer2_LCD.setObjectName("mixer2_LCD")
        self.horizontalLayout_8.addWidget(self.mixer2_LCD)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.mixer2_component_combobox = QtWidgets.QComboBox(self.groupBox_3)
        self.mixer2_component_combobox.setMinimumSize(QtCore.QSize(0, 22))
        self.mixer2_component_combobox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(13, 17, 23);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: transparent;\n"
" }\n"
"\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/Arrowhead-nottop-256.png);\n"
"     width: 7px;\n"
"     height: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: transparent;\n"
"}")
        self.mixer2_component_combobox.setObjectName("mixer2_component_combobox")
        self.mixer2_component_combobox.addItem("")
        self.mixer2_component_combobox.addItem("")
        self.mixer2_component_combobox.addItem("")
        self.mixer2_component_combobox.addItem("")
        self.mixer2_component_combobox.addItem("")
        self.mixer2_component_combobox.addItem("")
        self.mixer2_component_combobox.addItem("")
        self.verticalLayout_4.addWidget(self.mixer2_component_combobox)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(402, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.apply_component = QtWidgets.QPushButton(self.ComponentMixer, clicked = lambda: self.open_window())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_component.setFont(font)
        self.apply_component.setObjectName("apply_component")
        self.apply_component.setStyleSheet("""
            QPushButton#apply_component {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            
            QPushButton#apply_component:hover {
                background-color: #218838;
            }
            
            QPushButton#apply_component:pressed {
                background-color: #1e7e34;
            }
        """)
        self.horizontalLayout_9.addWidget(self.apply_component)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.mixer.addWidget(self.ComponentMixer)
        self.gridLayout_10.addWidget(self.MIxerbox, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.ImagesBox)

        self.retranslateUi(MainWindow)
        self.component_image1_comboBox.setCurrentIndex(0)
        self.component_image3_comboBox.setCurrentIndex(0)
        self.component_image_2_comboBox.setCurrentIndex(0)
        self.component_image4_comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.component_image1_comboBox.currentIndexChanged.connect(lambda : display_components(self.image_1,
                                                                                      self.component_image1_comboBox.currentIndex(),
                                                                                      self.component_image_1))
        
        self.component_image_2_comboBox.currentIndexChanged.connect(lambda : display_components(self.image_2,
                                                                                      self.component_image_2_comboBox.currentIndex(),
                                                                                      self.component_image_2))
        
        self.component_image3_comboBox.currentIndexChanged.connect(lambda : display_components(self.image_3,
                                                                                      self.component_image3_comboBox.currentIndex(),
                                                                                      self.component_image_3))
        
        self.component_image4_comboBox.currentIndexChanged.connect(lambda : display_components(self.image_4,
                                                                                      self.component_image4_comboBox.currentIndex(),
                                                                                      self.companent_image_4))
        
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Mixer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Image Mixer</span></p></body></html>"))
        self.groupBox_image1_2.setTitle(_translate("MainWindow", "Image 1"))
        self.output_imge1_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.output_imge1_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.component_image1_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.component_image1_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.component_image1_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.component_image1_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.component_image1_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.groupBox_image3.setTitle(_translate("MainWindow", "Image 3"))
        self.output_image3_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.output_image3_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.component_image3_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.component_image3_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.component_image3_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.component_image3_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.component_image3_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.groupBox_image1.setTitle(_translate("MainWindow", "Image 2"))
        self.output_image2_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.output_image2_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.component_image_2_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.component_image_2_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.component_image_2_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.component_image_2_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.component_image_2_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.groupBox_image2.setTitle(_translate("MainWindow", "Image 4"))
        self.output_image4_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.output_image4_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.component_image4_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.component_image4_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.component_image4_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.component_image4_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.component_image4_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.PereferenceBox.setTitle(_translate("MainWindow", "Mixer Preferences"))
        self.regions_radiobutton.setText(_translate("MainWindow", "Regions Mixer"))
        self.component_radiobutton.setText(_translate("MainWindow", "Components Mixer"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Pick Region:</span></p></body></html>"))
        self.outer_radiobutton.setText(_translate("MainWindow", "Outer"))
        self.inner_radiobutton.setText(_translate("MainWindow", "Inner"))
        self.region_LCD.setText(_translate("MainWindow", "100%"))
        self.apply_region.setText(_translate("MainWindow", "Apply"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Output 1:</span></p></body></html>"))
        self.mixer1_image_combobox.setItemText(0, _translate("MainWindow", "Image 1"))
        self.mixer1_image_combobox.setItemText(1, _translate("MainWindow", "Image 2"))
        self.mixer1_image_combobox.setItemText(2, _translate("MainWindow", "Image 3"))
        self.mixer1_image_combobox.setItemText(3, _translate("MainWindow", "Image 4"))
        self.mixer1_LCD.setText(_translate("MainWindow", "100%"))
        self.mixer1_component_combobox.setItemText(0, _translate("MainWindow", "Phase"))
        self.mixer1_component_combobox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.mixer1_component_combobox.setItemText(2, _translate("MainWindow", "Uniform Phase"))
        self.mixer1_component_combobox.setItemText(3, _translate("MainWindow", "Uniform Magnitude"))
        self.mixer1_component_combobox.setItemText(4, _translate("MainWindow", "Real"))
        self.mixer1_component_combobox.setItemText(5, _translate("MainWindow", "Imaginary"))
        self.mixer1_component_combobox.setItemText(6, _translate("MainWindow", "Full"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Output 2:</span></p></body></html>"))
        self.mixer2_image_combobox.setItemText(0, _translate("MainWindow", "Image 1"))
        self.mixer2_image_combobox.setItemText(1, _translate("MainWindow", "Image 2"))
        self.mixer2_image_combobox.setItemText(2, _translate("MainWindow", "Image 3"))
        self.mixer2_image_combobox.setItemText(3, _translate("MainWindow", "Image 4"))
        self.mixer2_LCD.setText(_translate("MainWindow", "100%"))
        self.mixer2_component_combobox.setItemText(0, _translate("MainWindow", "Phase"))
        self.mixer2_component_combobox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.mixer2_component_combobox.setItemText(2, _translate("MainWindow", "Uniform Phase"))
        self.mixer2_component_combobox.setItemText(3, _translate("MainWindow", "Uniform Magnitude"))
        self.mixer2_component_combobox.setItemText(4, _translate("MainWindow", "Real"))
        self.mixer2_component_combobox.setItemText(5, _translate("MainWindow", "Imaginary"))
        self.mixer2_component_combobox.setItemText(6, _translate("MainWindow", "Full"))
        self.apply_component.setText(_translate("MainWindow", "Apply"))
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #Maestro = ApplicationManager(ui,ui.DisplayedImages)
    MainWindow.show()
    sys.exit(app.exec_())
