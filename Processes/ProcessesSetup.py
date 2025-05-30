import psutil
from psutil._common import bytes2human


class Processes:
    def __init__(self):
        pass

    def get_info_for_Test(self):
        proc_dict = []
        for p in psutil.process_iter(["pid", "name", "exe", "memory_info", "cpu_percent"]):
            proc_dict.append(p.info)
        return proc_dict

    def clear_cache():
        psutil.process_iter.cache_clear()                                                                                                          
                                                                                                                  

            
        