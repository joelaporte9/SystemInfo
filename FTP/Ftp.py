import paramiko
import os

class ftp:
    def __init__(self, files=None, hostname=None, password=None, username=None, port=None):
        self.files = files
        self.hostname = hostname
        self.password = password
        self.username = username
        self.port = port

    def establish_connection(self, hostname, password, username, port):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policye(paramiko.AutoAddPolicy())
        ssh.connect(hostname, password, username, port)
        sftp_client = ssh.open_sftp()

        return sftp_client

    def send_file(self, filename):
        return True
        



        