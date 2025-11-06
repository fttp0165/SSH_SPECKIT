import paramiko

class SSHClient:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(self.hostname, username=self.username, password=self.password)
            return True
        except Exception:
            return False

    def send_command(self, command):
        if not self.client:
            raise Exception('Not connected')
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode()

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
            return True
        return False
