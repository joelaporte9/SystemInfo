import psutil

class cpu:
    def __init__(self, uptime=None, frequecny=None, usage_percent=None, ) -> None:
        self.uptime = uptime
        self.frequency = frequecny
        self.usage_percent = usage_percent

    def get_uptime(self):
        self.load = psutil.cpu_times()
        return self.load
    
    def get_cpu_frequency(self):
        self.frequency = psutil.cpu_freq()
        return self.frequency
     
    def get_usage_percent(self):
        self.usage_percent = psutil.cpu_percent(interval=1)
        return self.usage_percent
    




