import argparse
from ssh_client import SSHClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSH 指令執行工具")
    parser.add_argument("connect", help="連線指令", nargs='?')
    parser.add_argument("user_host", help="格式: user@host", nargs='?')
    parser.add_argument("-psw", "--password", help="SSH 密碼", required=True)
    parser.add_argument("-cmd", "--cmd", help="要執行的指令", required=True)
    args = parser.parse_args()

    if args.connect and args.user_host:
        if '@' not in args.user_host:
            print("user_host 格式錯誤，需為 user@host")
            exit(1)
        username, hostname = args.user_host.split('@', 1)
        client = SSHClient(hostname, username, args.password)
        if client.connect():
            output = client.send_command(args.cmd)
            print(output)
            client.close()
        else:
            print("SSH 連線失敗")
    else:
        print("請輸入 connect user@host -psw 密碼 -command 指令")

