#Process ID PID
#name
# CPU % used
# Mem % used
#create time
#exe
import psutil
from psutil._common import bytes2human


class Processes:
    def __init__(self, pid):
        self.pid = pid 
        # self.name = name
        # self.cpuPercent = cpuPercent
        # self.memPercent = memPercent
        # self.time = time
        # self.exe = exe


    def get_infor_for_Test(self):
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            self.pid = proc.info['pid']
            
        return self.pid
        