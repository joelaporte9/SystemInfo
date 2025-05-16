# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.diskData = QListView(self.centralwidget)
        self.diskData.setObjectName(u"diskData")
        self.diskData.setGeometry(QRect(610, 270, 171, 261))
        self.gpuData = QListView(self.centralwidget)
        self.gpuData.setObjectName(u"gpuData")
        self.gpuData.setGeometry(QRect(210, 270, 171, 261))
        self.memData = QListView(self.centralwidget)
        self.memData.setObjectName(u"memData")
        self.memData.setGeometry(QRect(410, 270, 171, 261))
        self.cpuData = QListView(self.centralwidget)
        self.cpuData.setObjectName(u"cpuData")
        self.cpuData.setGeometry(QRect(10, 270, 171, 261))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 270, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 270, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 270, 49, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(680, 270, 49, 16))
        self.netbtn = QPushButton(self.centralwidget)
        self.netbtn.setObjectName(u"netbtn")
        self.netbtn.setGeometry(QRect(630, 0, 75, 24))
        self.procbtn = QPushButton(self.centralwidget)
        self.procbtn.setObjectName(u"procbtn")
        self.procbtn.setGeometry(QRect(710, 0, 75, 24))
        self.systembtn = QPushButton(self.centralwidget)
        self.systembtn.setObjectName(u"systembtn")
        self.systembtn.setGeometry(QRect(550, 0, 75, 24))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 20, 791, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.user = QLabel(self.centralwidget)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(10, 10, 141, 16))
        self.ip = QLabel(self.centralwidget)
        self.ip.setObjectName(u"ip")
        self.ip.setGeometry(QRect(150, 10, 111, 16))
        self.login = QLabel(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(290, 10, 171, 16))
        self.cpuTemp = QLCDNumber(self.centralwidget)
        self.cpuTemp.setObjectName(u"cpuTemp")
        self.cpuTemp.setGeometry(QRect(120, 100, 121, 101))
        self.gputmp = QLCDNumber(self.centralwidget)
        self.gputmp.setObjectName(u"gputmp")
        self.gputmp.setGeometry(QRect(330, 100, 121, 101))
        self.fanspeed = QLCDNumber(self.centralwidget)
        self.fanspeed.setObjectName(u"fanspeed")
        self.fanspeed.setGeometry(QRect(530, 100, 121, 101))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 80, 71, 20))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(360, 80, 71, 20))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(560, 80, 71, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Memory", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.netbtn.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.procbtn.setText(QCoreApplication.translate("MainWindow", u"Proceses", None))
        self.systembtn.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.user.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.ip.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"System Login", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CPU TEMP", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"GPU TEMP", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FAN SPEED", None))
    # retranslateUi

