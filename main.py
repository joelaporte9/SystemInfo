import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from Ui.mainUi import Ui_MainWindow as MainUi
from Ui.FTP.SFTP import Ui_MainWindow as SftpUi
from System.SystemFunctionality import SystemFunc
from FTP.SftpFunctionality import SftpFunc

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_ui = MainUi()
        self.sftp_ui = SftpUi()
        self.system_func = SystemFunc(self.main_ui)
        self.sftp_func = SftpFunc(self.sftp_ui)
        self.main_ui.setupUi(self)
        self.system_func.user_label()
        self.system_func.user_login()
        self.system_func.user_host()
        self.system_func.disk_partition_info()
        self.system_func.virtual_memory_info()
        self.system_func.swap_memory_info()

        # Click the SFTP button
        self.main_ui.sftp.clicked.connect(self.sftp_func.sftp_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()


    sys.exit(app.exec())