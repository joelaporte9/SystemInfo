from PySide6.QtWidgets import QFileDialog
from SFTP.SftpSetup import SftpSetup

class SftpFunc(object):
    def __init__(self, ui):
        self.ui = ui

    def open_dialog(self):
        self.files, _ = QFileDialog.getOpenFileName(None, 'Single File', '*', '*.xlsm')
        self.ui.sourceFile.setText(str(self.files.split("/")[-1]))
    
    def cancel_button_func(self):
        self.ui.usernametxt.setText("")
        self.ui.passtxt.setText("")
        self.ui.hosttxt.setText("")
        self.ui.desFiletxtbx.setText("")

    def connect_ssh(self):
        self.hostname = self.ui.hosttxt.text()         
        self.username = self.ui.usernametxt.text()         
        self.password = self.ui.passtxt.text()         
        self.port = int(self.ui.porttxt.text())   
        self.destination = self.ui.desFiletxtbx.text() 
        sftp = SftpSetup(self.hostname, self.username,  self.password, self.port,  self.destination)
        try:
            sftp.establish_ssh_connection()
            
            #IF STATEMENT HERE FOR ERROR HANDELING 
            self.ui.connectlbl.setText("Connected!")
        except:
            self.ui.connectlbl.setText("Failed to connect")
    
   
        
         


        



          
      
           

        


