import psutil
from datetime import datetime

class user:
    def __init__(self, user=None, date=None, host=None ) -> None:
        self.user = user
        self.date = date
        self.host = host

    def get_user_login_date(self):
        return datetime.fromtimestamp(psutil.boot_time()).strftime("%A, %B %d, %Y %I:%M:%S")
    
    def get_user(self):
        for info in psutil.users():
            user = info.name
        return user
    
    def get_hostname(self):
        for info in psutil.users():
            host = info.host

            if not host:
                return "localhost"
            
        return host

    
    
    
    
       
