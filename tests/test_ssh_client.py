import pytest
from ssh_client import SSHClient

# TDD: 測試 SSH 連線、發送指令、關閉連線

def test_connect():
    client = SSHClient('192.168.1.1', 'root', '1234')
    assert client.connect() is True
    client.close()

def test_send_command():
    client = SSHClient('192.168.1.1', 'root', '1234')
    client.connect()
    output = client.send_command('echo hello')
    assert 'hello' in output
    client.close()

def test_close():
    client = SSHClient('192.168.1.1', 'root', '1234')
    client.connect()
    assert client.close() is True
