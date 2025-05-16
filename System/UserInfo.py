import psutil
from datetime import datetime

class user:
    def __init__(self, user=None, date=None, ip=None, ) -> None:
        self.user = user
        self.date = date

    def get_user_login_date(self):
        for info in psutil.users():
            date = datetime.fromtimestamp(info.started).strftime("%A, %B %d, %Y %I:%M:%S")

        return date
       
