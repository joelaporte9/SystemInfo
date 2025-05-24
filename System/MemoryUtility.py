import psutil
from psutil._common import bytes2human

class memory:

    def __init__(self, virtual_mem=None, swap_mem=None) -> list:
        self.virtual_mem = virtual_mem
        self.swap_mem = swap_mem
     
    def get_virtual_memory(self):
        virtual_mem = []
        vir_mem = psutil.virtual_memory()
        virtual_mem.append(bytes2human(vir_mem.total))
        virtual_mem.append(bytes2human(vir_mem.available))
        virtual_mem.append(vir_mem.percent)
        virtual_mem.append(bytes2human(vir_mem.used))
        virtual_mem.append(bytes2human(vir_mem.free))

        return virtual_mem
    
    def get_swap_memory(self):
        swap_memory = []
        swap_mem = psutil.swap_memory()
        swap_memory.append(bytes2human(swap_mem.total))
        swap_memory.append(bytes2human(swap_mem.used))
        swap_memory.append(bytes2human(swap_mem.free))
        swap_memory.append(swap_mem.percent)

        return swap_memory


    def memory_threshold(self):
        vir_mem_thresh = psutil.virtual_memory() 
        availible_mem = vir_mem_thresh.available
        threashold = 100 * 1024 * 1024

        if availible_mem <= threashold:
            return("warning")





