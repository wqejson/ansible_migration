from paramiko import SSHClient
from scp import SCPClient
import sys

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('185.181.231.54')

