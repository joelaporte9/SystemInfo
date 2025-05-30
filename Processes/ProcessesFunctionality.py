#Process ID PID
#name
# CPU % used
# Mem % used
#create time
#exe
from Processes.ProcessesSetup import Processes as ProcSetup
from PySide6 import QtWidgets

class ProcFunc:
    def __init__(self, ui):
        self.ui = ui 

    def clear_cache_btn(self):
        try:
            ProcSetup.clear_cache()
        except:
            pass
                                                                                                                     
    def display_info_for_Test(self):
        processes = ProcSetup()
        row = 0
        process = processes.get_info_for_Test()
        self.ui.tableWidget.setRowCount(len(process))
        for proc in process:
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(proc["pid"]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(proc["name"]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(proc["exe"]))
            
            row += 1





        
        

       


        