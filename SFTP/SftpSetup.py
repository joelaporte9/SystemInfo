import paramiko

class SftpSetup(object):
    def __init__(self,hostname, username, password, port, destination):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.destination = destination
        self.port = int(port)
      
    def establish_ssh_connection(self):      
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, username=self.username, password=self.password,  port=self.port, timeout=120.00)
        sftp_client = ssh.open_sftp()
        sftp_client.chdir(self.destination)
        
        return sftp_client
        