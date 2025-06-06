import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Ui.mainUi import Ui_MainWindow as MainUi
from System.SystemFunctionality import SystemFunc
from SFTP.SftpFunctionality import SftpFunc
from Processes.ProcessesFunctionality import ProcFunc
from Services.SerivicesFunctionality import SerFunc
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Window Setup
        self.main_ui = MainUi()
        self.sftp_func = SftpFunc(self.main_ui)
        self.system_func = SystemFunc(self.main_ui)
        self.proc_func = ProcFunc(self.main_ui)
        self.ser_func = SerFunc(self.main_ui)
        self.main_ui.setupUi(self)

        # PROCESS FUNCTIONALITY 
        #self.proc_func.display_info_for_Test()
        #self.main_ui.cclear.clicked.connect(self.proc_func.clear_cache_btn)

        # SERVICES FUNCTIONALITY 
        self.ser_func.display_S_info_for_Test()

        # SYSTEM FUNCTIONALITY
        self.system_func.user_label()
        self.system_func.user_login()
        self.system_func.user_host()
        self.system_func.disk_partition_info()
        self.system_func.virtual_memory_info()
        self.system_func.swap_memory_info()


        # SFTP FUNCTIONALITY
        self.main_ui.files.clicked.connect(self.sftp_func.open_dialog)
        self.main_ui.cancel.clicked.connect(self.sftp_func.cancel_button_func)
        self.main_ui.connect.clicked.connect(self.sftp_func.connect_ssh)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()


    sys.exit(app.exec())