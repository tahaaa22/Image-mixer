from PyQt5 import QtCore, QtGui, QtWidgets
from UI_Output import Ui_Output
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ApplicationManager import *
import sys, cv2
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def __init__(self):
        self.DisplayedImages = []
        
    def show_image(self):
        self.figure = plt.figure(facecolor='none', edgecolor='none', frameon= True)
        plt.rcParams['figure.figsize'] = [100, 100]
        plt.rcParams.update({'font.size' : 1})
        plt.axis('off')
        self.figure.sticky_edges.x[:]
        self.figure.sticky_edges.y[:]
        plt.axis('off')
        image = FigureCanvas(self.figure)
        #TODO: change it to be dynamic and gray image
        read_image = cv2.imread('placeholder.png') #by default as static
        plt.imshow(256 -read_image, extent=[0, read_image.shape[1], 0, read_image.shape[0]])
        plt.tight_layout()
        image.draw()
        self.figure.set_size_inches(read_image.shape[1] / 200, read_image.shape[0] / 200)
        return image
        
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
        MainWindow.resize(1147, 896)
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
        self.Image1_output_comboBox = QtWidgets.QComboBox(self.groupBox_image1_2)
        self.Image1_output_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.Image1_output_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: transparent;\n"
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
        self.Image1_output_comboBox.setObjectName("Image1_output_comboBox")
        self.Image1_output_comboBox.addItem("")
        self.Image1_output_comboBox.addItem("")
        self.gridLayout_6.addWidget(self.Image1_output_comboBox, 0, 0, 1, 1)
        self.Image1_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1_2)
        self.Image1_component_comboBox.setMinimumSize(QtCore.QSize(0, 22))
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
        self.gridLayout_6.addWidget(self.Image1_component_comboBox, 0, 1, 1, 1)
        # Create a Matplotlib figure and canvas
        self.image_1 = self.show_image()
        self.gridLayout_6.addWidget(self.image_1, 1, 0, 1, 1)
        # Create a Matplotlib figure and canvas
        self.Image1_component = self.show_image()
        self.gridLayout_6.addWidget(self.Image1_component, 1, 1, 1, 1)
        
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
        self.Image3_output_comboBox = QtWidgets.QComboBox(self.groupBox_image3)
        self.Image3_output_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.Image3_output_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: transparent;\n"
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
        self.Image3_output_comboBox.setObjectName("Image3_output_comboBox")
        self.Image3_output_comboBox.addItem("")
        self.Image3_output_comboBox.addItem("")
        self.gridLayout_7.addWidget(self.Image3_output_comboBox, 0, 0, 1, 1)
        self.Image3_component_comboBox = QtWidgets.QComboBox(self.groupBox_image3)
        self.Image3_component_comboBox.setMinimumSize(QtCore.QSize(0, 22))
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
        self.gridLayout_7.addWidget(self.Image3_component_comboBox, 0, 1, 1, 1)
       # Create a Matplotlib figure and canvas
        self.image_3 = self.show_image()
        self.gridLayout_7.addWidget(self.image_3, 1, 0, 1, 1)
        
        self.Image3_component= self.show_image()
        self.gridLayout_7.addWidget(self.Image3_component, 1, 1, 1, 1)
        
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
        self.Image2_output_comboBox = QtWidgets.QComboBox(self.groupBox_image1)
        self.Image2_output_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.Image2_output_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: transparent;\n"
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
        self.Image2_output_comboBox.setObjectName("Image2_output_comboBox")
        self.Image2_output_comboBox.addItem("")
        self.Image2_output_comboBox.addItem("")
        self.gridLayout_8.addWidget(self.Image2_output_comboBox, 0, 0, 1, 1)
        self.Image2_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1)
        self.Image2_component_comboBox.setMinimumSize(QtCore.QSize(0, 22))
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
        self.gridLayout_8.addWidget(self.Image2_component_comboBox, 0, 1, 1, 1)
        # Create a Matplotlib figure and canvas
        self.image_2 = self.show_image()
        self.gridLayout_8.addWidget(self.image_2, 1, 0, 1, 1)
        self.Image2_component= self.show_image()
        self.gridLayout_8.addWidget(self.Image2_component, 1, 1, 1, 1)
        
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
        self.Image4_output_comboBox = QtWidgets.QComboBox(self.groupBox_image2)
        self.Image4_output_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.Image4_output_comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Image4_output_comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    border-radius: 3px;\n"
"background-color: transparent;\n"
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
        self.Image4_output_comboBox.setObjectName("Image4_output_comboBox")
        self.Image4_output_comboBox.addItem("")
        self.Image4_output_comboBox.addItem("")
        self.gridLayout_9.addWidget(self.Image4_output_comboBox, 0, 0, 1, 1)
        self.Image4_component_comboBox = QtWidgets.QComboBox(self.groupBox_image2)
        self.Image4_component_comboBox.setMinimumSize(QtCore.QSize(0, 22))
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
        self.gridLayout_9.addWidget(self.Image4_component_comboBox, 0, 1, 1, 1)
        # Create a Matplotlib figure and canvas
        self.image_4 = self.show_image()
        self.gridLayout_9.addWidget(self.image_4, 1, 0, 1, 1)
        self.Image4_component= self.show_image()
        self.gridLayout_9.addWidget(self.Image4_component, 1, 1, 1, 1)
        
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
        self.RegionButton = QtWidgets.QRadioButton(self.PereferenceBox)
        self.RegionButton.setObjectName("RegionButton")
        #Connect the radio buttons' clicked signal to the slot
        self.RegionButton.clicked.connect(self.show_RegionBox)
        self.RegionButton.setChecked(True)
        self.gridLayout_4.addWidget(self.RegionButton, 0, 0, 1, 1)
        self.ComponentButton = QtWidgets.QRadioButton(self.PereferenceBox)
        self.ComponentButton.setObjectName("ComponentButton")
        self.ComponentButton.clicked.connect(self.show_ComponentMixer)
        self.gridLayout_4.addWidget(self.ComponentButton, 0, 1, 1, 1)
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MIxerbox)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(900, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.apply_region = QtWidgets.QPushButton(self.RegionBox, clicked = lambda: self.open_window())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_region.setFont(font)
        self.apply_region.setStyleSheet(" QPushButton#apply_region {\n"
"                background-color: #28a745;\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 5px 10px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            \n"
"            QPushButton#apply_region:hover {\n"
"                background-color: #218838;\n"
"            }\n"
"            \n"
"            QPushButton#apply_region:pressed {\n"
"                background-color: #1e7e34;\n"
"            }")
        self.apply_region.setObjectName("apply_region")
        self.horizontalLayout_11.addWidget(self.apply_region)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.RegionBox, 0, 0, 1, 1)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ComponentMixer)
        self.ComponentMixer.setVisible(False)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
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
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setStyleSheet("background-color: transparent;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.mixer1_image_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.mixer1_image_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.mixer1_image_comboBox.setStyleSheet("QComboBox\n"
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
        self.mixer1_image_comboBox.setObjectName("mixer1_image_comboBox")
        self.mixer1_image_comboBox.addItem("")
        self.mixer1_image_comboBox.addItem("")
        self.mixer1_image_comboBox.addItem("")
        self.mixer1_image_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.mixer1_image_comboBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mixer_component1_horizontalSlider = QtWidgets.QSlider(self.groupBox_3)
        self.mixer_component1_horizontalSlider.setMinimumSize(QtCore.QSize(160, 0))
        self.mixer_component1_horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mixer_component1_horizontalSlider.setStyleSheet("QSlider{\n"
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
        self.mixer_component1_horizontalSlider.setMaximum(100)
        self.mixer_component1_horizontalSlider.setProperty("value", 0)
        self.mixer_component1_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.mixer_component1_horizontalSlider.setObjectName("mixer_component1_horizontalSlider")
        self.horizontalLayout_6.addWidget(self.mixer_component1_horizontalSlider)
        self.mixer1_LCD = QtWidgets.QLCDNumber(self.groupBox_3)
        self.mixer1_LCD.setObjectName("mixer1_LCD")
        self.horizontalLayout_6.addWidget(self.mixer1_LCD)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
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
        self.verticalLayout_3.addWidget(self.mixer1_component_combobox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_12.addWidget(self.line_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setStyleSheet("background-color: transparent;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.mixer2_image_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.mixer2_image_comboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.mixer2_image_comboBox.setStyleSheet("QComboBox\n"
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
        self.mixer2_image_comboBox.setObjectName("mixer2_image_comboBox")
        self.mixer2_image_comboBox.addItem("")
        self.mixer2_image_comboBox.addItem("")
        self.mixer2_image_comboBox.addItem("")
        self.mixer2_image_comboBox.addItem("")
        self.horizontalLayout_17.addWidget(self.mixer2_image_comboBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        spacerItem3 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem3)
        self.horizontalLayout_16.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.mixer_component1_horizontalSlider_6 = QtWidgets.QSlider(self.groupBox_3)
        self.mixer_component1_horizontalSlider_6.setMinimumSize(QtCore.QSize(160, 0))
        self.mixer_component1_horizontalSlider_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mixer_component1_horizontalSlider_6.setStyleSheet("QSlider{\n"
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
        self.mixer_component1_horizontalSlider_6.setMaximum(100)
        self.mixer_component1_horizontalSlider_6.setProperty("value", 0)
        self.mixer_component1_horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.mixer_component1_horizontalSlider_6.setObjectName("mixer_component1_horizontalSlider_6")
        self.horizontalLayout_18.addWidget(self.mixer_component1_horizontalSlider_6)
        self.mixer2_LCD = QtWidgets.QLCDNumber(self.groupBox_3)
        self.mixer2_LCD.setObjectName("mixer2_LCD")
        self.horizontalLayout_18.addWidget(self.mixer2_LCD)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
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
        self.verticalLayout_11.addWidget(self.mixer2_component_combobox)
        self.horizontalLayout_16.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.verticalLayout_13.addWidget(self.groupBox_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(402, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.apply_component = QtWidgets.QPushButton(self.ComponentMixer, clicked = lambda: self.open_window())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_component.setFont(font)
        self.apply_component.setStyleSheet(" QPushButton#apply_component {\n"
"                background-color: #28a745;\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 5px 10px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            \n"
"            QPushButton#apply_component:hover {\n"
"                background-color: #218838;\n"
"            }\n"
"            \n"
"            QPushButton#apply_component:pressed {\n"
"                background-color: #1e7e34;\n"
"            }")
        self.apply_component.setObjectName("apply_component")
        self.horizontalLayout_9.addWidget(self.apply_component)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.ComponentMixer, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.MIxerbox, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.ImagesBox)

        self.retranslateUi(MainWindow)
        self.Image1_component_comboBox.setCurrentIndex(0)
        self.Image3_component_comboBox.setCurrentIndex(0)
        self.Image2_component_comboBox.setCurrentIndex(0)
        self.Image4_component_comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Image1_component_comboBox.currentIndexChanged.connect(lambda : display_components(self.Image1,
                                                                                      self.Image1_component_comboBox.currentIndex(),
                                                                                      self.Image1_component))
        
        self.Image2_component_comboBox.currentIndexChanged.connect(lambda : display_components(self.Image2,
                                                                                      self.Image2_component_comboBox.currentIndex(),
                                                                                      self.Image2_component))
        
        self.Image3_component_comboBox.currentIndexChanged.connect(lambda : display_components(self.Image3,
                                                                                      self.Image3_component_comboBox.currentIndex(),
                                                                                      self.Image3_component))
        
        self.Image4_component_comboBox.currentIndexChanged.connect(lambda : display_components(self.Image4,
                                                                                      self.Image4_component_comboBox.currentIndex(),
                                                                                      self.Image4_component))
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Image Mixer</span></p></body></html>"))
        self.groupBox_image1_2.setTitle(_translate("MainWindow", "Image 1"))
        self.Image1_output_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.Image1_output_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.Image1_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image1_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image1_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image1_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image1_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.groupBox_image3.setTitle(_translate("MainWindow", "Image 3"))
        self.Image3_output_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.Image3_output_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.Image3_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image3_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image3_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image3_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image3_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.groupBox_image1.setTitle(_translate("MainWindow", "Image 2"))
        self.Image2_output_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.Image2_output_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.Image2_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image2_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image2_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image2_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image2_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.groupBox_image2.setTitle(_translate("MainWindow", "Image 4"))
        self.Image4_output_comboBox.setItemText(0, _translate("MainWindow", "Output 1"))
        self.Image4_output_comboBox.setItemText(1, _translate("MainWindow", "Output 2"))
        self.Image4_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image4_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image4_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.Image4_component_comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.Image4_component_comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.PereferenceBox.setTitle(_translate("MainWindow", "Mixer Preferences"))
        self.RegionButton.setText(_translate("MainWindow", "Regions Mixer"))
        self.ComponentButton.setText(_translate("MainWindow", "Components Mixer"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Pick Region:</span></p></body></html>"))
        self.OuterButton.setText(_translate("MainWindow", "Outer"))
        self.InnerButton.setText(_translate("MainWindow", "Inner"))
        self.apply_region.setText(_translate("MainWindow", "Apply"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component 1:</span></p></body></html>"))
        self.mixer1_image_comboBox.setItemText(0, _translate("MainWindow", "Image 1"))
        self.mixer1_image_comboBox.setItemText(1, _translate("MainWindow", "Image 2"))
        self.mixer1_image_comboBox.setItemText(2, _translate("MainWindow", "Image 3"))
        self.mixer1_image_comboBox.setItemText(3, _translate("MainWindow", "Image 4"))
        self.mixer1_component_combobox.setItemText(0, _translate("MainWindow", "Phase"))
        self.mixer1_component_combobox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.mixer1_component_combobox.setItemText(2, _translate("MainWindow", "Real"))
        self.mixer1_component_combobox.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component 2:</span></p></body></html>"))
        self.mixer2_image_comboBox.setItemText(0, _translate("MainWindow", "Image 1"))
        self.mixer2_image_comboBox.setItemText(1, _translate("MainWindow", "Image 2"))
        self.mixer2_image_comboBox.setItemText(2, _translate("MainWindow", "Image 3"))
        self.mixer2_image_comboBox.setItemText(3, _translate("MainWindow", "Image 4"))
        self.mixer2_component_combobox.setItemText(0, _translate("MainWindow", "Phase"))
        self.mixer2_component_combobox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.mixer2_component_combobox.setItemText(2, _translate("MainWindow", "Real"))
        self.mixer2_component_combobox.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.apply_component.setText(_translate("MainWindow", "Apply"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #Maestro = ApplicationManager(ui,ui.DisplayedImages)
    MainWindow.show()
    sys.exit(app.exec_())
