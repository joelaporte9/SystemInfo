# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 29, 891, 501))
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.SFTP = QWidget()
        self.SFTP.setObjectName(u"SFTP")
        self.SFTP.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.connect = QPushButton(self.SFTP)
        self.connect.setObjectName(u"connect")
        self.connect.setGeometry(QRect(350, 260, 75, 24))
        self.hosttxt = QLineEdit(self.SFTP)
        self.hosttxt.setObjectName(u"hosttxt")
        self.hosttxt.setGeometry(QRect(280, 100, 141, 22))
        self.label_14 = QLabel(self.SFTP)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(510, 190, 61, 16))
        self.line_2 = QFrame(self.SFTP)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(200, 320, 481, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.usernametxt = QLineEdit(self.SFTP)
        self.usernametxt.setObjectName(u"usernametxt")
        self.usernametxt.setGeometry(QRect(280, 130, 141, 22))
        self.files = QToolButton(self.SFTP)
        self.files.setObjectName(u"files")
        self.files.setGeometry(QRect(550, 260, 71, 22))
        self.label_4 = QLabel(self.SFTP)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(208, 190, 49, 16))
        self.porttxt = QLineEdit(self.SFTP)
        self.porttxt.setObjectName(u"porttxt")
        self.porttxt.setGeometry(QRect(280, 190, 141, 22))
        self.label = QLabel(self.SFTP)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(208, 100, 61, 16))
        self.line_3 = QFrame(self.SFTP)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(440, 80, 20, 221))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.sourceFile = QLabel(self.SFTP)
        self.sourceFile.setObjectName(u"sourceFile")
        self.sourceFile.setGeometry(QRect(460, 210, 211, 16))
        self.label_5 = QLabel(self.SFTP)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 220, 71, 16))
        self.cancel = QPushButton(self.SFTP)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(270, 260, 75, 24))
        self.passtxt = QLineEdit(self.SFTP)
        self.passtxt.setObjectName(u"passtxt")
        self.passtxt.setGeometry(QRect(280, 160, 141, 22))
        self.label_2 = QLabel(self.SFTP)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(208, 130, 61, 16))
        self.desFiletxtbx = QLineEdit(self.SFTP)
        self.desFiletxtbx.setObjectName(u"desFiletxtbx")
        self.desFiletxtbx.setGeometry(QRect(282, 220, 141, 22))
        self.sendBtn = QPushButton(self.SFTP)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setGeometry(QRect(470, 260, 75, 24))
        self.label_3 = QLabel(self.SFTP)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(208, 160, 61, 16))
        self.label_7 = QLabel(self.SFTP)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(510, 130, 71, 16))
        self.destFile = QLabel(self.SFTP)
        self.destFile.setObjectName(u"destFile")
        self.destFile.setGeometry(QRect(460, 150, 211, 16))
        self.line_4 = QFrame(self.SFTP)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(200, 70, 481, 20))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5 = QFrame(self.SFTP)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(190, 80, 20, 251))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_6 = QFrame(self.SFTP)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(670, 80, 20, 251))
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.connectlbl = QLabel(self.SFTP)
        self.connectlbl.setObjectName(u"connectlbl")
        self.connectlbl.setGeometry(QRect(290, 300, 111, 16))
        self.tabWidget.addTab(self.SFTP, "")
        self.Services = QWidget()
        self.Services.setObjectName(u"Services")
        self.tableWidget_2 = QTableWidget(self.Services)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(15, 11, 851, 451))
        self.tableWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.addTab(self.Services, "")
        self.Processes = QWidget()
        self.Processes.setObjectName(u"Processes")
        self.tableWidget = QTableWidget(self.Processes)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 861, 441))
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.cclear = QPushButton(self.Processes)
        self.cclear.setObjectName(u"cclear")
        self.cclear.setGeometry(QRect(10, 450, 81, 24))
        self.tabWidget.addTab(self.Processes, "")
        self.System = QWidget()
        self.System.setObjectName(u"System")
        self.System.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cpuTemp = QLCDNumber(self.System)
        self.cpuTemp.setObjectName(u"cpuTemp")
        self.cpuTemp.setGeometry(QRect(30, 40, 141, 101))
        self.label_8 = QLabel(self.System)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 20, 71, 20))
        self.cpuFreq = QLCDNumber(self.System)
        self.cpuFreq.setObjectName(u"cpuFreq")
        self.cpuFreq.setGeometry(QRect(250, 40, 141, 101))
        self.label_28 = QLabel(self.System)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(280, 20, 91, 20))
        self.label_10 = QLabel(self.System)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(510, 20, 71, 20))
        self.gputmp = QLCDNumber(self.System)
        self.gputmp.setObjectName(u"gputmp")
        self.gputmp.setGeometry(QRect(470, 40, 141, 101))
        self.label_11 = QLabel(self.System)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(730, 20, 71, 20))
        self.fanspeed = QLCDNumber(self.System)
        self.fanspeed.setObjectName(u"fanspeed")
        self.fanspeed.setGeometry(QRect(690, 40, 141, 101))
        self.line_12 = QFrame(self.System)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(10, 210, 171, 20))
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_30 = QLabel(self.System)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(50, 200, 91, 20))
        self.cpuData = QListView(self.System)
        self.cpuData.setObjectName(u"cpuData")
        self.cpuData.setGeometry(QRect(10, 200, 171, 261))
        self.label_31 = QLabel(self.System)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(280, 200, 91, 20))
        self.gpuData = QListView(self.System)
        self.gpuData.setObjectName(u"gpuData")
        self.gpuData.setGeometry(QRect(240, 200, 171, 261))
        self.line_11 = QFrame(self.System)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(240, 210, 171, 20))
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_27 = QLabel(self.System)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(480, 340, 81, 16))
        self.vmemFree = QLabel(self.System)
        self.vmemFree.setObjectName(u"vmemFree")
        self.vmemFree.setGeometry(QRect(560, 300, 51, 16))
        self.line_9 = QFrame(self.System)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(470, 210, 171, 20))
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_17 = QLabel(self.System)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(480, 420, 49, 16))
        self.vmemAvail = QLabel(self.System)
        self.vmemAvail.setObjectName(u"vmemAvail")
        self.vmemAvail.setGeometry(QRect(560, 240, 51, 16))
        self.vmemUsed = QLabel(self.System)
        self.vmemUsed.setObjectName(u"vmemUsed")
        self.vmemUsed.setGeometry(QRect(560, 280, 51, 16))
        self.label_25 = QLabel(self.System)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(480, 300, 81, 16))
        self.label_21 = QLabel(self.System)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(480, 440, 49, 16))
        self.vmemTotal = QLabel(self.System)
        self.vmemTotal.setObjectName(u"vmemTotal")
        self.vmemTotal.setGeometry(QRect(560, 220, 49, 16))
        self.label_18 = QLabel(self.System)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(480, 380, 49, 16))
        self.smemFree = QLabel(self.System)
        self.smemFree.setObjectName(u"smemFree")
        self.smemFree.setGeometry(QRect(560, 420, 49, 16))
        self.label_20 = QLabel(self.System)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(480, 220, 49, 16))
        self.vmemperc = QLabel(self.System)
        self.vmemperc.setObjectName(u"vmemperc")
        self.vmemperc.setGeometry(QRect(560, 260, 51, 16))
        self.label_23 = QLabel(self.System)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(480, 260, 81, 16))
        self.label_19 = QLabel(self.System)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(510, 200, 91, 20))
        self.label_22 = QLabel(self.System)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(480, 240, 81, 16))
        self.line_8 = QFrame(self.System)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(470, 370, 171, 20))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_24 = QLabel(self.System)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(480, 280, 81, 16))
        self.smemused = QLabel(self.System)
        self.smemused.setObjectName(u"smemused")
        self.smemused.setGeometry(QRect(560, 400, 49, 16))
        self.vmemInact = QLabel(self.System)
        self.vmemInact.setObjectName(u"vmemInact")
        self.vmemInact.setGeometry(QRect(560, 340, 51, 16))
        self.perUsedSwap = QLabel(self.System)
        self.perUsedSwap.setObjectName(u"perUsedSwap")
        self.perUsedSwap.setGeometry(QRect(560, 440, 49, 16))
        self.label_15 = QLabel(self.System)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(480, 400, 49, 16))
        self.line_10 = QFrame(self.System)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(470, 350, 171, 20))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.smemTotal = QLabel(self.System)
        self.smemTotal.setObjectName(u"smemTotal")
        self.smemTotal.setGeometry(QRect(560, 380, 49, 16))
        self.memData = QListView(self.System)
        self.memData.setObjectName(u"memData")
        self.memData.setGeometry(QRect(470, 200, 171, 261))
        self.vmemActive = QLabel(self.System)
        self.vmemActive.setObjectName(u"vmemActive")
        self.vmemActive.setGeometry(QRect(560, 320, 51, 16))
        self.label_12 = QLabel(self.System)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(510, 360, 91, 20))
        self.label_26 = QLabel(self.System)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(480, 320, 81, 16))
        self.line_13 = QFrame(self.System)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(700, 330, 171, 20))
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_16 = QLabel(self.System)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(710, 250, 81, 16))
        self.line_14 = QFrame(self.System)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(700, 310, 171, 20))
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.disktotal = QLabel(self.System)
        self.disktotal.setObjectName(u"disktotal")
        self.disktotal.setGeometry(QRect(790, 340, 49, 16))
        self.diskMP = QLabel(self.System)
        self.diskMP.setObjectName(u"diskMP")
        self.diskMP.setGeometry(QRect(790, 250, 51, 16))
        self.label_32 = QLabel(self.System)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(710, 400, 49, 16))
        self.diskData = QListView(self.System)
        self.diskData.setObjectName(u"diskData")
        self.diskData.setGeometry(QRect(700, 200, 171, 261))
        self.label_33 = QLabel(self.System)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(750, 320, 91, 20))
        self.diskDev = QLabel(self.System)
        self.diskDev.setObjectName(u"diskDev")
        self.diskDev.setGeometry(QRect(790, 220, 49, 16))
        self.label_34 = QLabel(self.System)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(710, 220, 49, 16))
        self.label_13 = QLabel(self.System)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(740, 200, 91, 20))
        self.dsikfree = QLabel(self.System)
        self.dsikfree.setObjectName(u"dsikfree")
        self.dsikfree.setGeometry(QRect(790, 400, 49, 16))
        self.label_35 = QLabel(self.System)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(710, 340, 49, 16))
        self.label_36 = QLabel(self.System)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(710, 430, 49, 16))
        self.line_15 = QFrame(self.System)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(700, 210, 171, 20))
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)
        self.perUsed = QLabel(self.System)
        self.perUsed.setObjectName(u"perUsed")
        self.perUsed.setGeometry(QRect(790, 430, 49, 16))
        self.label_37 = QLabel(self.System)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(710, 370, 49, 16))
        self.diskused = QLabel(self.System)
        self.diskused.setObjectName(u"diskused")
        self.diskused.setGeometry(QRect(790, 370, 49, 16))
        self.tabWidget.addTab(self.System, "")
        self.diskData.raise_()
        self.memData.raise_()
        self.gpuData.raise_()
        self.cpuData.raise_()
        self.cpuTemp.raise_()
        self.label_8.raise_()
        self.cpuFreq.raise_()
        self.label_28.raise_()
        self.label_10.raise_()
        self.gputmp.raise_()
        self.label_11.raise_()
        self.fanspeed.raise_()
        self.line_12.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.line_11.raise_()
        self.label_27.raise_()
        self.vmemFree.raise_()
        self.line_9.raise_()
        self.label_17.raise_()
        self.vmemAvail.raise_()
        self.vmemUsed.raise_()
        self.label_25.raise_()
        self.label_21.raise_()
        self.vmemTotal.raise_()
        self.label_18.raise_()
        self.smemFree.raise_()
        self.label_20.raise_()
        self.vmemperc.raise_()
        self.label_23.raise_()
        self.label_19.raise_()
        self.label_22.raise_()
        self.line_8.raise_()
        self.label_24.raise_()
        self.smemused.raise_()
        self.vmemInact.raise_()
        self.perUsedSwap.raise_()
        self.label_15.raise_()
        self.line_10.raise_()
        self.smemTotal.raise_()
        self.vmemActive.raise_()
        self.label_12.raise_()
        self.label_26.raise_()
        self.line_13.raise_()
        self.label_16.raise_()
        self.line_14.raise_()
        self.disktotal.raise_()
        self.diskMP.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.diskDev.raise_()
        self.label_34.raise_()
        self.label_13.raise_()
        self.dsikfree.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.line_15.raise_()
        self.perUsed.raise_()
        self.label_37.raise_()
        self.diskused.raise_()
        self.hostname = QLabel(self.centralwidget)
        self.hostname.setObjectName(u"hostname")
        self.hostname.setGeometry(QRect(150, 0, 121, 16))
        self.loginSince_2 = QLabel(self.centralwidget)
        self.loginSince_2.setObjectName(u"loginSince_2")
        self.loginSince_2.setGeometry(QRect(280, 0, 61, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 10, 901, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.login = QLabel(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(350, 0, 171, 16))
        self.user = QLabel(self.centralwidget)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(10, 0, 141, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 903, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Source:", None))
        self.files.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Host:", None))
        self.sourceFile.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destination:", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.sendBtn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Destination:", None))
        self.destFile.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.connectlbl.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SFTP), QCoreApplication.translate("MainWindow", u"SFTP", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Bin Path", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Owner", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Start Type", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Services), QCoreApplication.translate("MainWindow", u"Services", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"exe", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Memory Usage", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"CPU Usage", None));
        self.cclear.setText(QCoreApplication.translate("MainWindow", u"Clear Cache", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Processes), QCoreApplication.translate("MainWindow", u"Processes", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CPU TEMP", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"CPU Frequency", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GPU TEMP", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"FAN SPEED", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"CPU Information", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"GPU Information", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.vmemFree.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Free:", None))
        self.vmemAvail.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.vmemUsed.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Free:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.vmemTotal.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.smemFree.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.vmemperc.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Virtual Memory", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Available", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Used:", None))
        self.smemused.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.vmemInact.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.perUsedSwap.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Used:", None))
        self.smemTotal.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.vmemActive.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Swap Memory", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Active:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Mount Point:", None))
        self.disktotal.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.diskMP.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Free:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.diskDev.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Device:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Disk Partitions", None))
        self.dsikfree.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.perUsed.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Used:", None))
        self.diskused.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.System), QCoreApplication.translate("MainWindow", u"System", None))
        self.hostname.setText(QCoreApplication.translate("MainWindow", u"hostname", None))
        self.loginSince_2.setText(QCoreApplication.translate("MainWindow", u"Last Login:", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"System Login", None))
        self.user.setText(QCoreApplication.translate("MainWindow", u"User:", None))
    # retranslateUi

