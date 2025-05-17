import psutil

class disk:

    def __init__(self, disk_part=None) -> list:
        self.disk_part = disk_part

    def get_disk_partitions(self):
        disk_part = []
        for info in psutil.disk_partitions():
            disk_part.append(info.device)
            disk_part.append(info.mountpoint)

            usage = psutil.disk_usage(info.mountpoint)

            disk_part.append(usage.total)
            disk_part.append(usage.used)
            disk_part.append(usage.free)
            disk_part.append(usage.percent)

        return disk_part

    

        
        
