import psutil
from psutil._common import bytes2human

class ServicSetup:

    def __init__(self, list_services):
        self.list_services = list_services

    def get_services():
        for service in psutil.win_service_iter():
            list_services = [service]
            return list_services