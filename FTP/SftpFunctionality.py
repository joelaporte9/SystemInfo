import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile
from Ui.FTP.SFTP import Ui_MainWindow as SftpUI

class SftpFunc(object):
    def __init__(self,ui):
          self.ui = SftpUI()
          self.ui = ui
        
    def sftp_window(self):
            self.window = QMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.files.clicked.connect(self.open_dialog)

    def open_dialog(self):
        filename, _ = QFileDialog.getOpenFileName(None, 'Single File', '*', '*.xlsm')
        self.ui.filename1.setText(str(filename.split("/")[-1]))

    def establish_ssh_connection(self):
        return True




          
      
           

        


