from System.UserInfo import user
from System.Disk import disk
from System.MemoryUtility import memory

class SystemFunc(object):
    def __init__(self, ui):
        self.ui = ui
        
# User information
    def user_label(self):
            login_user = user()
            username = login_user.get_user()
            self.ui.user.setText(username)
            # clibrary = ctypes.CDLL("C:/Users/joela/OneDrive/Desktop/Programming/SystemInfo/System/Gpu.so")
            # hello = clibrary.myprint()

    def user_login(self):
            login_date = user()
            login = login_date.get_user_login_date()
            self.ui.login.setText(login)

    def user_host(self):
            user_host = user()
            host = user_host.get_hostname()
            self.ui.hostname.setText(host)

    # functions handle disk related tasks

    def disk_partition_info(self):
            disk_part = disk()
            partition_info = disk_part.get_disk_partitions()
            self.ui.diskDev.setText(partition_info[0])
            self.ui.diskMP.setText(partition_info[1])

            # Display usage informatiom
            self.ui.disktotal.setText(str(partition_info[2]))
            self.ui.diskused.setText(str(partition_info[3]))
            self.ui.dsikfree.setText(str(partition_info[4]))
            self.ui.perUsed.setText(str(partition_info[5]))

    # functions to handle memory related tasks

    def virtual_memory_info(self):
            vir_mem = memory()
            vir_mem_info = vir_mem.get_virtual_memory()
            self.ui.vmemTotal.setText(str(vir_mem_info[0]))
            self.ui.vmemAvail.setText(str(vir_mem_info[1]))
            self.ui.vmemperc.setText(str(vir_mem_info[2]))
            self.ui.vmemUsed.setText(str(vir_mem_info[3]))
            self.ui.vmemFree.setText(str(vir_mem_info[4]))

    def swap_memory_info(self):
            swap_mem = memory()
            swap_mem_info = swap_mem.get_swap_memory()
            self.ui.smemTotal.setText(str(swap_mem_info[0]))
            self.ui.smemused.setText(str(swap_mem_info[1]))
            self.ui.smemFree.setText(str(swap_mem_info[2]))
            self.ui.perUsedSwap.setText(str(swap_mem_info[3]))