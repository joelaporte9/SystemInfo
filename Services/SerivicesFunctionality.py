from Services.ServicesSetup import ServicSetup as ServSetup
from PySide6 import QtWidgets


class SerFunc:
    def __init__(self, ui):
        self.ui = ui 
                                                                                                                     
    def display_S_info_for_Test(self):
        services = ServSetup()
        row = 0
        service = services.get_services()
        self.ui.tableWidget.setRowCount(len(service))
        for serv in service:
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(serv["name"]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(serv["binpath"]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(serv["username"]))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(serv["start_type"]))
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(serv["pid"]))
            self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(serv["status"]))

            
            row += 1
