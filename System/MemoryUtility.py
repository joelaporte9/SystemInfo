import psutil

class memory:
    def __init__(self, virtual_mem) -> None:
        self.virtual_mem = virtual_mem
     
    def get_virtual_mem_stats(self):
        self.virtual_mem = psutil.virtual_memory()
        return self.virtual_mem
    
    def memory_threshold():
        virual_men = psutil.virtual_memory() 
        availible_mem = virual_men.available
        threashold = 100 * 1024 * 1024  # 100MB

        if availible_mem <= threashold:
            print ("warning")





