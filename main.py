import paramiko


HOST = "192.168.1.1"  # Replace with your SSH server
USERNAME = "root"    # Replace with your username
KEY_PATH = "C:/Users/BENNYLIN.SPORTON/.ssh/id_rsa"  # Replace with your private key path
COMMAND = "ls"                # Replace with the command you want to run



def ssh_execute_command(host, username, key_path, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        key = paramiko.RSAKey.from_private_key_file(key_path)
        client.connect(hostname=host, username=username, pkey=key)
        stdin, stdout, stderr = client.exec_command(command)
        print("Output:")
        print(stdout.read().decode())
        print("Errors:")
        print(stderr.read().decode())
    except Exception as e:
        print(f"SSH connection failed: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    ssh_execute_command(HOST, USERNAME, KEY_PATH, COMMAND)
