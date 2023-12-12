from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import ImageView
from PyQt5.QtCore import QEvent
import sys
from UI_Output import Ui_Output
from ApplicationManager import *


class Ui_MainWindow(object):

    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Output()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 904)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #1e1e2f;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
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
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ImagesBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
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
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_image1_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Image1_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image1_component_comboBox.sizePolicy().hasHeightForWidth())
        self.Image1_component_comboBox.setSizePolicy(sizePolicy)
        self.Image1_component_comboBox.setMinimumSize(QtCore.QSize(176, 22))
        self.Image1_component_comboBox.setStyleSheet("QComboBox\n"
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
        self.Image1_component_comboBox.setMaxCount(2147483646)
        self.Image1_component_comboBox.setObjectName("Image1_component_comboBox")
        self.Image1_component_comboBox.addItem("")
        self.Image1_component_comboBox.addItem("")
        self.Image1_component_comboBox.addItem("")
        self.Image1_component_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.Image1_component_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Image_1 = ImageView(self.groupBox_image1_2)
        self.Image_1.setObjectName("Image_1")
        self.horizontalLayout_4.addWidget(self.Image_1)
        self.Image1_component = ImageView(self.groupBox_image1_2)
        self.Image1_component.setObjectName("Image1_component")
        self.horizontalLayout_4.addWidget(self.Image1_component)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_image1_2)
        self.label_14.setStyleSheet("background-color: transparent;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.image1_component1_slider = QtWidgets.QSlider(self.groupBox_image1_2)
        self.image1_component1_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.image1_component1_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image1_component1_slider.setStyleSheet("QSlider{\n"
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
        self.image1_component1_slider.setMaximum(100)
        self.image1_component1_slider.setProperty("value", 0)
        self.image1_component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image1_component1_slider.setObjectName("image1_component1_slider")
        self.horizontalLayout_6.addWidget(self.image1_component1_slider)
        self.image1_component1_LCD = QtWidgets.QLCDNumber(self.groupBox_image1_2)
        self.image1_component1_LCD.setObjectName("image1_component1_LCD")
        self.horizontalLayout_6.addWidget(self.image1_component1_LCD)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_35.addWidget(self.groupBox_image1_2)
        self.groupBox_image1_3 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image1_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1_3.sizePolicy().hasHeightForWidth())
        self.groupBox_image1_3.setSizePolicy(sizePolicy)
        self.groupBox_image1_3.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1_3.setStyleSheet("QGroupBox {\n"
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
        self.groupBox_image1_3.setObjectName("groupBox_image1_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_image1_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.Image2_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image2_component_comboBox.sizePolicy().hasHeightForWidth())
        self.Image2_component_comboBox.setSizePolicy(sizePolicy)
        self.Image2_component_comboBox.setMinimumSize(QtCore.QSize(176, 22))
        self.Image2_component_comboBox.setStyleSheet("QComboBox\n"
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
        self.Image2_component_comboBox.setMaxCount(2147483646)
        self.Image2_component_comboBox.setObjectName("Image2_component_comboBox")
        self.Image2_component_comboBox.addItem("")
        self.Image2_component_comboBox.addItem("")
        self.Image2_component_comboBox.addItem("")
        self.Image2_component_comboBox.addItem("")
        self.horizontalLayout_12.addWidget(self.Image2_component_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Image_2 = ImageView(self.groupBox_image1_3)
        self.Image_2.setObjectName("Image_2")
        self.horizontalLayout_14.addWidget(self.Image_2)
        self.Image2_component = ImageView(self.groupBox_image1_3)
        self.Image2_component.setObjectName("Image2_component")
        self.horizontalLayout_14.addWidget(self.Image2_component)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_image1_3)
        self.label_17.setStyleSheet("background-color: transparent;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.image2_component1_slider = QtWidgets.QSlider(self.groupBox_image1_3)
        self.image2_component1_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.image2_component1_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image2_component1_slider.setStyleSheet("QSlider{\n"
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
        self.image2_component1_slider.setMaximum(100)
        self.image2_component1_slider.setProperty("value", 0)
        self.image2_component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image2_component1_slider.setObjectName("image2_component1_slider")
        self.horizontalLayout_19.addWidget(self.image2_component1_slider)
        self.image2_component1_LCD = QtWidgets.QLCDNumber(self.groupBox_image1_3)
        self.image2_component1_LCD.setObjectName("image2_component1_LCD")
        self.horizontalLayout_19.addWidget(self.image2_component1_LCD)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_35.addWidget(self.groupBox_image1_3)
        self.verticalLayout.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.groupBox_image1_5 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image1_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1_5.sizePolicy().hasHeightForWidth())
        self.groupBox_image1_5.setSizePolicy(sizePolicy)
        self.groupBox_image1_5.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1_5.setStyleSheet("QGroupBox {\n"
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
        self.groupBox_image1_5.setObjectName("groupBox_image1_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_image1_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem2 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem2)
        self.Image3_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image3_component_comboBox.sizePolicy().hasHeightForWidth())
        self.Image3_component_comboBox.setSizePolicy(sizePolicy)
        self.Image3_component_comboBox.setMinimumSize(QtCore.QSize(176, 22))
        self.Image3_component_comboBox.setStyleSheet("QComboBox\n"
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
        self.Image3_component_comboBox.setMaxCount(2147483646)
        self.Image3_component_comboBox.setObjectName("Image3_component_comboBox")
        self.Image3_component_comboBox.addItem("")
        self.Image3_component_comboBox.addItem("")
        self.Image3_component_comboBox.addItem("")
        self.Image3_component_comboBox.addItem("")
        self.horizontalLayout_28.addWidget(self.Image3_component_comboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.Image_3 = ImageView(self.groupBox_image1_5)
        self.Image_3.setObjectName("Image_3")
        self.horizontalLayout_29.addWidget(self.Image_3)
        self.Image3_component = ImageView(self.groupBox_image1_5)
        self.Image3_component.setObjectName("Image3_component")
        self.horizontalLayout_29.addWidget(self.Image3_component)
        self.verticalLayout_6.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_22 = QtWidgets.QLabel(self.groupBox_image1_5)
        self.label_22.setStyleSheet("background-color: transparent;")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_30.addWidget(self.label_22)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.image3_component1_slider = QtWidgets.QSlider(self.groupBox_image1_5)
        self.image3_component1_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.image3_component1_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image3_component1_slider.setStyleSheet("QSlider{\n"
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
        self.image3_component1_slider.setMaximum(100)
        self.image3_component1_slider.setProperty("value", 0)
        self.image3_component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image3_component1_slider.setObjectName("image3_component1_slider")
        self.horizontalLayout_31.addWidget(self.image3_component1_slider)
        self.image3_component1_LCD = QtWidgets.QLCDNumber(self.groupBox_image1_5)
        self.image3_component1_LCD.setObjectName("image3_component1_LCD")
        self.horizontalLayout_31.addWidget(self.image3_component1_LCD)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)
        self.verticalLayout_6.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.horizontalLayout_32.addLayout(self.horizontalLayout_33)
        self.verticalLayout_6.addLayout(self.horizontalLayout_32)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_34.addWidget(self.groupBox_image1_5)
        self.groupBox_image1_4 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image1_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1_4.sizePolicy().hasHeightForWidth())
        self.groupBox_image1_4.setSizePolicy(sizePolicy)
        self.groupBox_image1_4.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1_4.setStyleSheet("QGroupBox {\n"
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
        self.groupBox_image1_4.setObjectName("groupBox_image1_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_image1_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem3 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem3)
        self.Image4_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image4_component_comboBox.sizePolicy().hasHeightForWidth())
        self.Image4_component_comboBox.setSizePolicy(sizePolicy)
        self.Image4_component_comboBox.setMinimumSize(QtCore.QSize(176, 22))
        self.Image4_component_comboBox.setStyleSheet("QComboBox\n"
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
        self.Image4_component_comboBox.setMaxCount(2147483646)
        self.Image4_component_comboBox.setObjectName("Image4_component_comboBox")
        self.Image4_component_comboBox.addItem("")
        self.Image4_component_comboBox.addItem("")
        self.Image4_component_comboBox.addItem("")
        self.Image4_component_comboBox.addItem("")
        self.horizontalLayout_22.addWidget(self.Image4_component_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.Image_4 = ImageView(self.groupBox_image1_4)
        self.Image_4.setObjectName("Image_4")
        self.horizontalLayout_23.addWidget(self.Image_4)
        self.Image4_component = ImageView(self.groupBox_image1_4)
        self.Image4_component.setObjectName("Image4_component")
        self.horizontalLayout_23.addWidget(self.Image4_component)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_20 = QtWidgets.QLabel(self.groupBox_image1_4)
        self.label_20.setStyleSheet("background-color: transparent;")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_24.addWidget(self.label_20)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.image4_component1_slider = QtWidgets.QSlider(self.groupBox_image1_4)
        self.image4_component1_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.image4_component1_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image4_component1_slider.setStyleSheet("QSlider{\n"
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
        self.image4_component1_slider.setMaximum(100)
        self.image4_component1_slider.setProperty("value", 0)
        self.image4_component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image4_component1_slider.setObjectName("image4_component1_slider")
        self.horizontalLayout_25.addWidget(self.image4_component1_slider)
        self.image4_component1_LCD = QtWidgets.QLCDNumber(self.groupBox_image1_4)
        self.image4_component1_LCD.setObjectName("image4_component1_LCD")
        self.horizontalLayout_25.addWidget(self.image4_component1_LCD)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)
        self.verticalLayout_4.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_34.addWidget(self.groupBox_image1_4)
        self.verticalLayout.addLayout(self.horizontalLayout_34)
        self.gridLayout_7.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.ImagesBox)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.RegionBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegionBox_2.sizePolicy().hasHeightForWidth())
        self.RegionBox_2.setSizePolicy(sizePolicy)
        self.RegionBox_2.setStyleSheet("QGroupBox {\n"
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
        self.RegionBox_2.setObjectName("RegionBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.RegionBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem4 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.component_radioButton = QtWidgets.QRadioButton(self.RegionBox_2)
        self.component_radioButton.setObjectName("component_radioButton")
        self.component_radioButton.setChecked(True)
        self.horizontalLayout_17.addWidget(self.component_radioButton)
        self.region_button = QtWidgets.QRadioButton(self.RegionBox_2)
        self.region_button.setObjectName("region_button")
        self.horizontalLayout_17.addWidget(self.region_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.gridLayout_8.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.RegionBox_2)
        self.RegionBox = QtWidgets.QGroupBox(self.centralwidget)
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.RegionBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_16 = QtWidgets.QLabel(self.RegionBox)
        self.label_16.setStyleSheet("background-color: transparent;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_13.addWidget(self.label_16)
        spacerItem5 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.OuterButton = QtWidgets.QRadioButton(self.RegionBox)
        self.OuterButton.setObjectName("OuterButton")
        self.horizontalLayout_10.addWidget(self.OuterButton)
        self.InnerButton = QtWidgets.QRadioButton(self.RegionBox)
        self.InnerButton.setObjectName("InnerButton")
        self.horizontalLayout_10.addWidget(self.InnerButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RegionSlider = QtWidgets.QSlider(self.RegionBox)
        self.RegionSlider.setMinimumSize(QtCore.QSize(160, 0))
        self.RegionSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RegionSlider.setStyleSheet("QSlider{\n"
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
        self.RegionSlider.setMaximum(100)
        self.RegionSlider.setProperty("value", 0)
        self.RegionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RegionSlider.setObjectName("RegionSlider")
        self.horizontalLayout_2.addWidget(self.RegionSlider)
        self.region_LCD = QtWidgets.QLCDNumber(self.RegionBox)
        self.region_LCD.setMinimumSize(QtCore.QSize(0, 0))
        self.region_LCD.setMaximumSize(QtCore.QSize(80, 16777215))
        self.region_LCD.setObjectName("region_LCD")
        self.horizontalLayout_2.addWidget(self.region_LCD)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.RegionBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
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
                                        "border-style: outset;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QGroupBox::title  {\n"
                                        "    subcontrol-origin: margin;\n"
                                        "    subcontrol-position: top left;\n"
                                        "    padding: -5px 0px 0px 0px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}")
        self.PereferenceBox.setTitle("")
        self.PereferenceBox.setObjectName("PereferenceBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.PereferenceBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.output1_button = QtWidgets.QRadioButton(self.PereferenceBox)
        self.output1_button.setObjectName("output1_button")
        self.output1_button.setChecked(True)
        self.horizontalLayout_9.addWidget(self.output1_button)
        self.output2_button = QtWidgets.QRadioButton(self.PereferenceBox)
        self.output2_button.setObjectName("output2_button")
        self.horizontalLayout_9.addWidget(self.output2_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.apply_button = QtWidgets.QPushButton(self.PereferenceBox, clicked = lambda: MAESTRO.mix())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        self.apply_button.setMaximumSize(QtCore.QSize(234, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_button.setFont(font)
        self.apply_button.setStyleSheet(" QPushButton#apply_button {\n"
                                        "                background-color: #28a745;\n"
                                        "                color: white;\n"
                                        "                border: none;\n"
                                        "                padding: 5px 10px;\n"
                                        "                border-radius: 5px;\n"
                                        "            }\n"
                                        "            \n"
                                        "            QPushButton#apply_button:hover {\n"
                                        "                background-color: #218838;\n"
                                        "            }\n"
                                        "            \n"
                                        "            QPushButton#apply_button:pressed {\n"
                                        "                background-color: #1e7e34;\n"
                                        "            }")
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_11.addWidget(self.apply_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.PereferenceBox)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.gridLayout_9.addLayout(self.verticalLayout_10, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.ImagesBox)

        self.retranslateUi(MainWindow)
        self.Image1_component_comboBox.setCurrentIndex(0)
        self.Image2_component_comboBox.setCurrentIndex(0)
        self.Image3_component_comboBox.setCurrentIndex(0)
        self.Image4_component_comboBox.setCurrentIndex(0)
        self.image1_component1_slider.valueChanged['int'].connect(self.image1_component1_LCD.display)  # type: ignore
        self.image2_component1_slider.valueChanged['int'].connect(self.image2_component1_LCD.display)  # type: ignore
        self.image3_component1_slider.valueChanged['int'].connect(self.image3_component1_LCD.display)  # type: ignore
        self.image4_component1_slider.valueChanged['int'].connect(self.image4_component1_LCD.display)  # type: ignore
        self.RegionSlider.valueChanged['int'].connect(self.region_LCD.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.RegionSlider.valueChanged.connect(lambda: MAESTRO.region_mix())

        ImageViews = [self.Image_1,self.Image1_component,self.Image_2,self.Image2_component,self.Image_3,self.Image3_component,
                      self.Image_4,self.Image4_component]

        for image in ImageViews:
                image.ui.histogram.hide()
                image.ui.roiBtn.hide()
                image.ui.menuBtn.hide()

        self.component_connections() # Connecting combobox IndexChanged to display new component

        # Do NOT delete this repetition
        # self.Image1_component_comboBox.currentIndexChanged.connect(lambda: MAESTRO.view_component(0,self.Image1_component_comboBox.currentIndex()))
        # self.Image2_component_comboBox.currentIndexChanged.connect(lambda: MAESTRO.view_component(1,self.Image2_component_comboBox.currentIndex()))
        # self.Image3_component_comboBox.currentIndexChanged.connect(lambda: MAESTRO.view_component(2,self.Image3_component_comboBox.currentIndex()))
        # self.Image4_component_comboBox.currentIndexChanged.connect(lambda: MAESTRO.view_component(3,self.Image4_component_comboBox.currentIndex()))

        # ComponentImageViews = [self.Image1_component,self.Image2_component,self.Image3_component,self.Image4_component]
        # background_color = QColor(255, 255, 255)
        # for image in ComponentImageViews:
        #     image.ui.graphicsView.setBackground(background_color)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Mixer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Image Mixer</span></p></body></html>"))
        self.groupBox_image1_2.setTitle(_translate("MainWindow", "Image 1"))
        self.Image1_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image1_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image1_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image1_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image1_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component :</span></p></body></html>"))
        self.groupBox_image1_3.setTitle(_translate("MainWindow", "Image 2"))
        self.Image2_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image2_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image2_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image2_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image2_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component :</span></p></body></html>"))
        self.groupBox_image1_5.setTitle(_translate("MainWindow", "Image 3"))
        self.Image3_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image3_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image3_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image3_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image3_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component :</span></p></body></html>"))
        self.groupBox_image1_4.setTitle(_translate("MainWindow", "Image 4"))
        self.Image4_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image4_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image4_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image4_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image4_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component :</span></p></body></html>"))
        self.RegionBox_2.setTitle(_translate("MainWindow", "Mixer Preferences"))
        self.component_radioButton.setText(_translate("MainWindow", "Component"))
        self.region_button.setText(_translate("MainWindow", "Region"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Pick Region:</span></p></body></html>"))
        self.OuterButton.setText(_translate("MainWindow", "Outer"))
        self.InnerButton.setText(_translate("MainWindow", "Inner"))
        self.output1_button.setText(_translate("MainWindow", "Output 1"))
        self.output2_button.setText(_translate("MainWindow", "Output 2"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))


    def component_connections(self):
        # TODO Super interesting phenomenon to be explained!
        # https://stackoverflow.com/questions/2295290/what-do-lambda-function-closures-capture
        component_comboboxes = [self.Image1_component_comboBox, self.Image2_component_comboBox, self.Image3_component_comboBox, self.Image4_component_comboBox]
        for i in range(4):
            # component_comboboxes[i].currentIndexChanged.connect(lambda: MAESTRO.view_component(i, component_comboboxes[i].currentIndex()))
            component_comboboxes[i].currentIndexChanged.connect(lambda index, i=i: MAESTRO.view_component(i, index))

class ImageView(ImageView):
    def mouseDoubleClickEvent(self, event):
        MAESTRO.load_image(self)


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MAESTRO = AppManager(ui)
        MainWindow.show()
        sys.exit(app.exec_())
