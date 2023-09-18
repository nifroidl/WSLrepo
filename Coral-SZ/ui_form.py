# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextBrowser, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1287, 703)
        icon = QIcon()
        icon.addFile(u"resources/47798062.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionWhite = QAction(MainWindow)
        self.actionWhite.setObjectName(u"actionWhite")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionConnect_Device = QAction(MainWindow)
        self.actionConnect_Device.setObjectName(u"actionConnect_Device")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 5))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 5, 0, 1, 4)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 0, 2, 4, 1)

        self.Buttons_Widget = QWidget(self.centralwidget)
        self.Buttons_Widget.setObjectName(u"Buttons_Widget")
        self.Buttons_Widget.setMaximumSize(QSize(16777215, 60))
        self.Button_HLayout = QHBoxLayout(self.Buttons_Widget)
        self.Button_HLayout.setObjectName(u"Button_HLayout")
        self.pB_PrepareDataset = QPushButton(self.Buttons_Widget)
        self.pB_PrepareDataset.setObjectName(u"pB_PrepareDataset")

        self.Button_HLayout.addWidget(self.pB_PrepareDataset)

        self.pB_Train = QPushButton(self.Buttons_Widget)
        self.pB_Train.setObjectName(u"pB_Train")
        self.pB_Train.setEnabled(True)

        self.Button_HLayout.addWidget(self.pB_Train)

        self.pB_Test = QPushButton(self.Buttons_Widget)
        self.pB_Test.setObjectName(u"pB_Test")
        self.pB_Test.setEnabled(False)

        self.Button_HLayout.addWidget(self.pB_Test)

        self.pB_RunModel = QPushButton(self.Buttons_Widget)
        self.pB_RunModel.setObjectName(u"pB_RunModel")
        self.pB_RunModel.setEnabled(False)

        self.Button_HLayout.addWidget(self.pB_RunModel)

        self.cB_Stream = QComboBox(self.Buttons_Widget)
        self.cB_Stream.addItem("")
        self.cB_Stream.addItem("")
        self.cB_Stream.setObjectName(u"cB_Stream")
        self.cB_Stream.setEnabled(False)

        self.Button_HLayout.addWidget(self.cB_Stream)


        self.gridLayout_4.addWidget(self.Buttons_Widget, 11, 0, 1, 4)

        self.Input_Widget = QWidget(self.centralwidget)
        self.Input_Widget.setObjectName(u"Input_Widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_Widget.sizePolicy().hasHeightForWidth())
        self.Input_Widget.setSizePolicy(sizePolicy)
        self.Input_Widget.setMaximumSize(QSize(16777215, 16777215))
        self.Input_Grid = QGridLayout(self.Input_Widget)
        self.Input_Grid.setObjectName(u"Input_Grid")
        self.Input_Grid.setContentsMargins(-1, 20, -1, 0)
        self.label_14 = QLabel(self.Input_Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"")

        self.Input_Grid.addWidget(self.label_14, 0, 0, 1, 4)

        self.toolButton_TrainImages = QToolButton(self.Input_Widget)
        self.toolButton_TrainImages.setObjectName(u"toolButton_TrainImages")
        self.toolButton_TrainImages.setEnabled(True)

        self.Input_Grid.addWidget(self.toolButton_TrainImages, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Input_Grid.addItem(self.horizontalSpacer_2, 0, 5, 6, 1)

        self.toolButton_TrainAnnotations = QToolButton(self.Input_Widget)
        self.toolButton_TrainAnnotations.setObjectName(u"toolButton_TrainAnnotations")

        self.Input_Grid.addWidget(self.toolButton_TrainAnnotations, 4, 2, 1, 1)

        self.label_13 = QLabel(self.Input_Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))
        self.label_13.setMaximumSize(QSize(150, 20))

        self.Input_Grid.addWidget(self.label_13, 5, 0, 1, 1)

        self.textBrowser_NumberOfClasses = QTextBrowser(self.Input_Widget)
        self.textBrowser_NumberOfClasses.setObjectName(u"textBrowser_NumberOfClasses")
        self.textBrowser_NumberOfClasses.setEnabled(False)
        self.textBrowser_NumberOfClasses.setMaximumSize(QSize(200, 26))
        self.textBrowser_NumberOfClasses.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_NumberOfClasses.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_NumberOfClasses.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Input_Grid.addWidget(self.textBrowser_NumberOfClasses, 5, 4, 1, 1)

        self.checkBox_FileFormat = QComboBox(self.Input_Widget)
        self.checkBox_FileFormat.addItem("")
        self.checkBox_FileFormat.addItem("")
        self.checkBox_FileFormat.setObjectName(u"checkBox_FileFormat")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_FileFormat.sizePolicy().hasHeightForWidth())
        self.checkBox_FileFormat.setSizePolicy(sizePolicy1)
        self.checkBox_FileFormat.setMaximumSize(QSize(50, 16777215))

        self.Input_Grid.addWidget(self.checkBox_FileFormat, 3, 3, 1, 1)

        self.textBrowser_TrainLabels = QTextBrowser(self.Input_Widget)
        self.textBrowser_TrainLabels.setObjectName(u"textBrowser_TrainLabels")
        self.textBrowser_TrainLabels.setEnabled(False)
        self.textBrowser_TrainLabels.setMaximumSize(QSize(200, 26))
        self.textBrowser_TrainLabels.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_TrainLabels.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_TrainLabels.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Input_Grid.addWidget(self.textBrowser_TrainLabels, 5, 1, 1, 1)

        self.toolButton_TrainLabels = QToolButton(self.Input_Widget)
        self.toolButton_TrainLabels.setObjectName(u"toolButton_TrainLabels")
        self.toolButton_TrainLabels.setStyleSheet(u"")
        self.toolButton_TrainLabels.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.Input_Grid.addWidget(self.toolButton_TrainLabels, 5, 2, 1, 1)

        self.label_12 = QLabel(self.Input_Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 0))
        self.label_12.setMaximumSize(QSize(150, 20))

        self.Input_Grid.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_19 = QLabel(self.Input_Widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(150, 0))

        self.Input_Grid.addWidget(self.label_19, 5, 3, 1, 1)

        self.textBrowser_TrainAnnotations = QTextBrowser(self.Input_Widget)
        self.textBrowser_TrainAnnotations.setObjectName(u"textBrowser_TrainAnnotations")
        self.textBrowser_TrainAnnotations.setEnabled(False)
        self.textBrowser_TrainAnnotations.setMaximumSize(QSize(200, 26))
        self.textBrowser_TrainAnnotations.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_TrainAnnotations.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_TrainAnnotations.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Input_Grid.addWidget(self.textBrowser_TrainAnnotations, 4, 1, 1, 1)

        self.label_11 = QLabel(self.Input_Widget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setMaximumSize(QSize(150, 20))

        self.Input_Grid.addWidget(self.label_11, 3, 0, 1, 1)

        self.textBrowser_TrainImages = QTextBrowser(self.Input_Widget)
        self.textBrowser_TrainImages.setObjectName(u"textBrowser_TrainImages")
        self.textBrowser_TrainImages.setEnabled(False)
        self.textBrowser_TrainImages.setMaximumSize(QSize(200, 26))
        self.textBrowser_TrainImages.setMouseTracking(True)
        self.textBrowser_TrainImages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_TrainImages.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_TrainImages.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_TrainImages.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Input_Grid.addWidget(self.textBrowser_TrainImages, 3, 1, 1, 1)

        self.checkBox_SplitDataset = QCheckBox(self.Input_Widget)
        self.checkBox_SplitDataset.setObjectName(u"checkBox_SplitDataset")
        self.checkBox_SplitDataset.setChecked(False)

        self.Input_Grid.addWidget(self.checkBox_SplitDataset, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.Input_Widget, 0, 0, 1, 1)

        self.SplitDataset_Widget = QWidget(self.centralwidget)
        self.SplitDataset_Widget.setObjectName(u"SplitDataset_Widget")
        self.SplitDataset_Widget.setEnabled(False)
        sizePolicy.setHeightForWidth(self.SplitDataset_Widget.sizePolicy().hasHeightForWidth())
        self.SplitDataset_Widget.setSizePolicy(sizePolicy)
        self.SplitDataset_Grid = QGridLayout(self.SplitDataset_Widget)
        self.SplitDataset_Grid.setObjectName(u"SplitDataset_Grid")
        self.SplitDataset_Grid.setContentsMargins(-1, -1, -1, 0)
        self.textBrowser_TestAnnotations = QTextBrowser(self.SplitDataset_Widget)
        self.textBrowser_TestAnnotations.setObjectName(u"textBrowser_TestAnnotations")
        self.textBrowser_TestAnnotations.setEnabled(False)
        self.textBrowser_TestAnnotations.setMaximumSize(QSize(200, 26))
        self.textBrowser_TestAnnotations.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_TestAnnotations.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_TestAnnotations.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.SplitDataset_Grid.addWidget(self.textBrowser_TestAnnotations, 2, 5, 1, 1)

        self.toolButton_TestImages = QToolButton(self.SplitDataset_Widget)
        self.toolButton_TestImages.setObjectName(u"toolButton_TestImages")

        self.SplitDataset_Grid.addWidget(self.toolButton_TestImages, 0, 6, 1, 1)

        self.label_4 = QLabel(self.SplitDataset_Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setMaximumSize(QSize(150, 20))

        self.SplitDataset_Grid.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_9 = QLabel(self.SplitDataset_Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 0))

        self.SplitDataset_Grid.addWidget(self.label_9, 2, 3, 1, 1)

        self.textBrowser_ValidateAnnotations = QTextBrowser(self.SplitDataset_Widget)
        self.textBrowser_ValidateAnnotations.setObjectName(u"textBrowser_ValidateAnnotations")
        self.textBrowser_ValidateAnnotations.setEnabled(False)
        self.textBrowser_ValidateAnnotations.setMaximumSize(QSize(200, 26))
        self.textBrowser_ValidateAnnotations.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_ValidateAnnotations.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_ValidateAnnotations.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.SplitDataset_Grid.addWidget(self.textBrowser_ValidateAnnotations, 2, 1, 1, 1)

        self.textBrowser_ValidateImages = QTextBrowser(self.SplitDataset_Widget)
        self.textBrowser_ValidateImages.setObjectName(u"textBrowser_ValidateImages")
        self.textBrowser_ValidateImages.setEnabled(False)
        self.textBrowser_ValidateImages.setMaximumSize(QSize(200, 26))
        self.textBrowser_ValidateImages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_ValidateImages.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_ValidateImages.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.SplitDataset_Grid.addWidget(self.textBrowser_ValidateImages, 0, 1, 1, 1)

        self.toolButton_ValidateImages = QToolButton(self.SplitDataset_Widget)
        self.toolButton_ValidateImages.setObjectName(u"toolButton_ValidateImages")

        self.SplitDataset_Grid.addWidget(self.toolButton_ValidateImages, 0, 2, 1, 1)

        self.toolButton_ValidateAnnotations = QToolButton(self.SplitDataset_Widget)
        self.toolButton_ValidateAnnotations.setObjectName(u"toolButton_ValidateAnnotations")

        self.SplitDataset_Grid.addWidget(self.toolButton_ValidateAnnotations, 2, 2, 1, 1)

        self.toolButton_TestAnnotations = QToolButton(self.SplitDataset_Widget)
        self.toolButton_TestAnnotations.setObjectName(u"toolButton_TestAnnotations")

        self.SplitDataset_Grid.addWidget(self.toolButton_TestAnnotations, 2, 6, 1, 1)

        self.label_10 = QLabel(self.SplitDataset_Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))

        self.SplitDataset_Grid.addWidget(self.label_10, 0, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SplitDataset_Grid.addItem(self.horizontalSpacer_6, 0, 7, 1, 1)

        self.textBrowser_TestImages = QTextBrowser(self.SplitDataset_Widget)
        self.textBrowser_TestImages.setObjectName(u"textBrowser_TestImages")
        self.textBrowser_TestImages.setEnabled(False)
        self.textBrowser_TestImages.setMaximumSize(QSize(200, 26))
        self.textBrowser_TestImages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_TestImages.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_TestImages.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.SplitDataset_Grid.addWidget(self.textBrowser_TestImages, 0, 5, 1, 1)

        self.label_7 = QLabel(self.SplitDataset_Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(150, 0))
        self.label_7.setMaximumSize(QSize(150, 20))

        self.SplitDataset_Grid.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_3 = QLabel(self.SplitDataset_Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.SplitDataset_Grid.addWidget(self.label_3, 3, 0, 1, 1)

        self.doubleSpinBox_TestSplitRate = QDoubleSpinBox(self.SplitDataset_Widget)
        self.doubleSpinBox_TestSplitRate.setObjectName(u"doubleSpinBox_TestSplitRate")
        self.doubleSpinBox_TestSplitRate.setMinimumSize(QSize(50, 0))
        self.doubleSpinBox_TestSplitRate.setMaximumSize(QSize(50, 16777215))
        self.doubleSpinBox_TestSplitRate.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.doubleSpinBox_TestSplitRate.setMaximum(1.000000000000000)
        self.doubleSpinBox_TestSplitRate.setSingleStep(0.010000000000000)
        self.doubleSpinBox_TestSplitRate.setValue(0.200000000000000)

        self.SplitDataset_Grid.addWidget(self.doubleSpinBox_TestSplitRate, 3, 1, 1, 1)

        self.label_8 = QLabel(self.SplitDataset_Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(110, 0))
        self.label_8.setMaximumSize(QSize(60, 16777215))

        self.SplitDataset_Grid.addWidget(self.label_8, 3, 3, 1, 1)

        self.doubleSpinBox_ValidateSplitRate = QDoubleSpinBox(self.SplitDataset_Widget)
        self.doubleSpinBox_ValidateSplitRate.setObjectName(u"doubleSpinBox_ValidateSplitRate")
        self.doubleSpinBox_ValidateSplitRate.setMinimumSize(QSize(40, 0))
        self.doubleSpinBox_ValidateSplitRate.setMaximumSize(QSize(50, 16777215))
        self.doubleSpinBox_ValidateSplitRate.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.doubleSpinBox_ValidateSplitRate.setMaximum(1.000000000000000)
        self.doubleSpinBox_ValidateSplitRate.setSingleStep(0.010000000000000)
        self.doubleSpinBox_ValidateSplitRate.setValue(0.200000000000000)

        self.SplitDataset_Grid.addWidget(self.doubleSpinBox_ValidateSplitRate, 3, 5, 1, 1)


        self.gridLayout_4.addWidget(self.SplitDataset_Widget, 1, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 12, 0, 1, 4)

        self.TrainParameter_Widget = QWidget(self.centralwidget)
        self.TrainParameter_Widget.setObjectName(u"TrainParameter_Widget")
        self.TrainParameter_Widget.setMaximumSize(QSize(16777215, 100))
        self.TrainParameter = QGridLayout(self.TrainParameter_Widget)
        self.TrainParameter.setObjectName(u"TrainParameter")
        self.TrainParameter.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_RunModelSettings = QGridLayout()
        self.gridLayout_RunModelSettings.setObjectName(u"gridLayout_RunModelSettings")
        self.label_LabelsForModel = QLabel(self.TrainParameter_Widget)
        self.label_LabelsForModel.setObjectName(u"label_LabelsForModel")
        self.label_LabelsForModel.setMaximumSize(QSize(16777215, 26))

        self.gridLayout_RunModelSettings.addWidget(self.label_LabelsForModel, 2, 0, 1, 1)

        self.textBrowser_LabelsForModel = QTextBrowser(self.TrainParameter_Widget)
        self.textBrowser_LabelsForModel.setObjectName(u"textBrowser_LabelsForModel")
        self.textBrowser_LabelsForModel.setMaximumSize(QSize(16777215, 26))

        self.gridLayout_RunModelSettings.addWidget(self.textBrowser_LabelsForModel, 2, 1, 1, 1)

        self.label_ModelToRun = QLabel(self.TrainParameter_Widget)
        self.label_ModelToRun.setObjectName(u"label_ModelToRun")
        self.label_ModelToRun.setMaximumSize(QSize(16777215, 26))

        self.gridLayout_RunModelSettings.addWidget(self.label_ModelToRun, 1, 0, 1, 1)

        self.textBrowser_ModelToRun = QTextBrowser(self.TrainParameter_Widget)
        self.textBrowser_ModelToRun.setObjectName(u"textBrowser_ModelToRun")
        self.textBrowser_ModelToRun.setMaximumSize(QSize(16777215, 26))

        self.gridLayout_RunModelSettings.addWidget(self.textBrowser_ModelToRun, 1, 1, 1, 1)

        self.toolButton_ModelToRun = QToolButton(self.TrainParameter_Widget)
        self.toolButton_ModelToRun.setObjectName(u"toolButton_ModelToRun")

        self.gridLayout_RunModelSettings.addWidget(self.toolButton_ModelToRun, 1, 2, 1, 1)

        self.toolButton_LabelsForModel = QToolButton(self.TrainParameter_Widget)
        self.toolButton_LabelsForModel.setObjectName(u"toolButton_LabelsForModel")

        self.gridLayout_RunModelSettings.addWidget(self.toolButton_LabelsForModel, 2, 2, 1, 1)


        self.TrainParameter.addLayout(self.gridLayout_RunModelSettings, 0, 8, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.TrainParameter.addItem(self.horizontalSpacer_3, 0, 7, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.TrainParameter_Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(85, 0))

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.spinBox_Batch = QSpinBox(self.TrainParameter_Widget)
        self.spinBox_Batch.setObjectName(u"spinBox_Batch")
        self.spinBox_Batch.setMinimumSize(QSize(100, 0))
        self.spinBox_Batch.setMinimum(1)
        self.spinBox_Batch.setMaximum(1000)
        self.spinBox_Batch.setValue(5)

        self.gridLayout_2.addWidget(self.spinBox_Batch, 0, 4, 1, 1)

        self.spinBox_Epochs = QSpinBox(self.TrainParameter_Widget)
        self.spinBox_Epochs.setObjectName(u"spinBox_Epochs")
        self.spinBox_Epochs.setMinimumSize(QSize(100, 0))
        self.spinBox_Epochs.setMinimum(1)
        self.spinBox_Epochs.setMaximum(1000)
        self.spinBox_Epochs.setValue(1)

        self.gridLayout_2.addWidget(self.spinBox_Epochs, 0, 2, 1, 1)

        self.label_6 = QLabel(self.TrainParameter_Widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_5 = QLabel(self.TrainParameter_Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 25))

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)


        self.TrainParameter.addLayout(self.gridLayout_2, 0, 6, 1, 1)


        self.gridLayout_4.addWidget(self.TrainParameter_Widget, 10, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")

        self.gridLayout_4.addWidget(self.label, 13, 0, 1, 4)

        self.Output_Widget = QWidget(self.centralwidget)
        self.Output_Widget.setObjectName(u"Output_Widget")
        self.Output_Grid = QGridLayout(self.Output_Widget)
        self.Output_Grid.setObjectName(u"Output_Grid")
        self.Output_Grid.setContentsMargins(-1, 0, -1, -1)
        self.checkBox_Quantization = QCheckBox(self.Output_Widget)
        self.checkBox_Quantization.setObjectName(u"checkBox_Quantization")
        self.checkBox_Quantization.setChecked(True)

        self.Output_Grid.addWidget(self.checkBox_Quantization, 8, 0, 1, 4)

        self.toolButton_ModelOutput = QToolButton(self.Output_Widget)
        self.toolButton_ModelOutput.setObjectName(u"toolButton_ModelOutput")

        self.Output_Grid.addWidget(self.toolButton_ModelOutput, 6, 3, 1, 1)

        self.textBrowser_ModelOutput = QTextBrowser(self.Output_Widget)
        self.textBrowser_ModelOutput.setObjectName(u"textBrowser_ModelOutput")
        self.textBrowser_ModelOutput.setEnabled(False)
        self.textBrowser_ModelOutput.setMaximumSize(QSize(200, 26))
        self.textBrowser_ModelOutput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_ModelOutput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_ModelOutput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Output_Grid.addWidget(self.textBrowser_ModelOutput, 6, 2, 1, 1)

        self.checkBox_CompileForEdgeTPU = QCheckBox(self.Output_Widget)
        self.checkBox_CompileForEdgeTPU.setObjectName(u"checkBox_CompileForEdgeTPU")
        self.checkBox_CompileForEdgeTPU.setChecked(True)

        self.Output_Grid.addWidget(self.checkBox_CompileForEdgeTPU, 7, 0, 1, 4)

        self.comboBox_Model = QComboBox(self.Output_Widget)
        self.comboBox_Model.addItem("")
        self.comboBox_Model.addItem("")
        self.comboBox_Model.addItem("")
        self.comboBox_Model.setObjectName(u"comboBox_Model")
        self.comboBox_Model.setMaximumSize(QSize(200, 16777215))

        self.Output_Grid.addWidget(self.comboBox_Model, 2, 0, 1, 3)

        self.label_17 = QLabel(self.Output_Widget)
        self.label_17.setObjectName(u"label_17")

        self.Output_Grid.addWidget(self.label_17, 6, 0, 1, 1)

        self.label_15 = QLabel(self.Output_Widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")

        self.Output_Grid.addWidget(self.label_15, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.Output_Widget, 0, 3, 4, 1)

        self.textBrowserProgess = QTextBrowser(self.centralwidget)
        self.textBrowserProgess.setObjectName(u"textBrowserProgess")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textBrowserProgess.sizePolicy().hasHeightForWidth())
        self.textBrowserProgess.setSizePolicy(sizePolicy3)
        self.textBrowserProgess.setMinimumSize(QSize(0, 200))
        self.textBrowserProgess.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.textBrowserProgess, 14, 0, 1, 4)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)

        self.gridLayout_4.addWidget(self.widget_2, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1287, 19))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuTheme = QMenu(self.menuSettings)
        self.menuTheme.setObjectName(u"menuTheme")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.menuTheme.menuAction())
        self.menuSettings.addAction(self.actionConnect_Device)
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionWhite)

        self.retranslateUi(MainWindow)
        self.checkBox_SplitDataset.toggled.connect(self.SplitDataset_Widget.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TrainUsIn - AI Training User Interface", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionWhite.setText(QCoreApplication.translate("MainWindow", u"White", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionConnect_Device.setText(QCoreApplication.translate("MainWindow", u"Connect Device", None))
        self.pB_PrepareDataset.setText(QCoreApplication.translate("MainWindow", u"Prepare Dataset", None))
        self.pB_Train.setText(QCoreApplication.translate("MainWindow", u"Train and Export", None))
        self.pB_Test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.pB_RunModel.setText(QCoreApplication.translate("MainWindow", u"Run Model on:", None))
        self.cB_Stream.setItemText(0, QCoreApplication.translate("MainWindow", u"File", None))
        self.cB_Stream.setItemText(1, QCoreApplication.translate("MainWindow", u"Stream", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_14.setProperty("class", QCoreApplication.translate("MainWindow", u"Header", None))
        self.toolButton_TrainImages.setText("")
        self.toolButton_TrainImages.setProperty("class", QCoreApplication.translate("MainWindow", u"folder", None))
        self.toolButton_TrainAnnotations.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Labels File", None))
        self.checkBox_FileFormat.setItemText(0, QCoreApplication.translate("MainWindow", u"png", None))
        self.checkBox_FileFormat.setItemText(1, QCoreApplication.translate("MainWindow", u"jpg", None))

        self.toolButton_TrainLabels.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Annotations Folder", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Number of Classes", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dataset Images Folder", None))
        self.checkBox_SplitDataset.setText(QCoreApplication.translate("MainWindow", u"Is your dataset already split?", None))
        self.toolButton_TestImages.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"V. Annotations Folder", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"T. Annotations Folder", None))
        self.toolButton_ValidateImages.setText("")
        self.toolButton_ValidateAnnotations.setText("")
        self.toolButton_TestAnnotations.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Test Images Folder", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Validate Images Folder", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Split Rate", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Split Rate", None))
        self.label_LabelsForModel.setText(QCoreApplication.translate("MainWindow", u"Labels for Model", None))
        self.label_ModelToRun.setText(QCoreApplication.translate("MainWindow", u"Model To Run", None))
        self.toolButton_ModelToRun.setText("")
        self.toolButton_LabelsForModel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Epochs", None))
        self.spinBox_Epochs.setPrefix("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Batch", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Training Parameter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Progress:", None))
        self.label.setProperty("class", QCoreApplication.translate("MainWindow", u"Header", None))
        self.checkBox_Quantization.setText(QCoreApplication.translate("MainWindow", u"Quantization (fp16)", None))
        self.toolButton_ModelOutput.setText("")
        self.checkBox_CompileForEdgeTPU.setText(QCoreApplication.translate("MainWindow", u"Compile for Edge TPU", None))
        self.comboBox_Model.setItemText(0, QCoreApplication.translate("MainWindow", u"EffifentDet-Lite0", None))
        self.comboBox_Model.setItemText(1, QCoreApplication.translate("MainWindow", u"EffifentDet-Lite1", None))
        self.comboBox_Model.setItemText(2, QCoreApplication.translate("MainWindow", u"EffifentDet-Lite2", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Model Output", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_15.setProperty("class", QCoreApplication.translate("MainWindow", u"Header", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

