# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogConnectDevice.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_DialogConnectDevice(object):
    def setupUi(self, DialogConnectDevice):
        if not DialogConnectDevice.objectName():
            DialogConnectDevice.setObjectName(u"DialogConnectDevice")
        DialogConnectDevice.resize(400, 300)
        self.listWidget = QListWidget(DialogConnectDevice)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 41, 141, 171))
        self.gridLayoutWidget = QWidget(DialogConnectDevice)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 220, 311, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_Search = QPushButton(self.gridLayoutWidget)
        self.pb_Search.setObjectName(u"pb_Search")

        self.gridLayout.addWidget(self.pb_Search, 1, 0, 1, 1)

        self.pb_Attach = QPushButton(self.gridLayoutWidget)
        self.pb_Attach.setObjectName(u"pb_Attach")

        self.gridLayout.addWidget(self.pb_Attach, 1, 1, 1, 1)

        self.pb_Detach = QPushButton(self.gridLayoutWidget)
        self.pb_Detach.setObjectName(u"pb_Detach")

        self.gridLayout.addWidget(self.pb_Detach, 1, 2, 1, 1)

        self.label = QLabel(DialogConnectDevice)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 16))
        self.label_2 = QLabel(DialogConnectDevice)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 20, 111, 16))
        self.gridLayoutWidget_2 = QWidget(DialogConnectDevice)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(180, 40, 206, 116))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_Manufacturer = QLabel(self.gridLayoutWidget_2)
        self.label_Manufacturer.setObjectName(u"label_Manufacturer")
        self.label_Manufacturer.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_Manufacturer, 1, 1, 1, 1)

        self.label_Name = QLabel(self.gridLayoutWidget_2)
        self.label_Name.setObjectName(u"label_Name")
        self.label_Name.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_Name, 0, 1, 1, 1)

        self.label_BusId = QLabel(self.gridLayoutWidget_2)
        self.label_BusId.setObjectName(u"label_BusId")
        self.label_BusId.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_BusId, 3, 1, 1, 1)

        self.label_VIDPID = QLabel(self.gridLayoutWidget_2)
        self.label_VIDPID.setObjectName(u"label_VIDPID")
        self.label_VIDPID.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_VIDPID, 4, 1, 1, 1)

        self.label_Port = QLabel(self.gridLayoutWidget_2)
        self.label_Port.setObjectName(u"label_Port")
        self.label_Port.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_Port, 6, 1, 1, 1)

        self.label_5 = QLabel(DialogConnectDevice)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(412, 130, 76, 78))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(DialogConnectDevice)

        QMetaObject.connectSlotsByName(DialogConnectDevice)
    # setupUi

    def retranslateUi(self, DialogConnectDevice):
        DialogConnectDevice.setWindowTitle(QCoreApplication.translate("DialogConnectDevice", u"Dialog", None))
        self.pb_Search.setText(QCoreApplication.translate("DialogConnectDevice", u"Search", None))
        self.pb_Attach.setText(QCoreApplication.translate("DialogConnectDevice", u"Attach", None))
        self.pb_Detach.setText(QCoreApplication.translate("DialogConnectDevice", u"Detach", None))
        self.label.setText(QCoreApplication.translate("DialogConnectDevice", u"Available Devices", None))
        self.label_2.setText(QCoreApplication.translate("DialogConnectDevice", u"Attached Device", None))
        self.label_13.setText(QCoreApplication.translate("DialogConnectDevice", u"Manufacturer", None))
        self.label_11.setText(QCoreApplication.translate("DialogConnectDevice", u"VID:PID", None))
        self.label_7.setText(QCoreApplication.translate("DialogConnectDevice", u"Port", None))
        self.label_6.setText(QCoreApplication.translate("DialogConnectDevice", u"BUS-ID", None))
        self.label_4.setText(QCoreApplication.translate("DialogConnectDevice", u"Name", None))
        self.label_Manufacturer.setText("")
        self.label_Name.setText(QCoreApplication.translate("DialogConnectDevice", u"No device attached", None))
        self.label_BusId.setText("")
        self.label_VIDPID.setText("")
        self.label_Port.setText("")
        self.label_5.setText(QCoreApplication.translate("DialogConnectDevice", u"TextLabel", None))
    # retranslateUi

