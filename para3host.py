import paramiko
import time
from netmiko import ConnectHandler

ip_address = "172.16.7.2"
username = "iana2"
password = "0Rb1tal2!"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username,
                   password=password, look_for_keys=False, allow_agent=False)

#print("Successful Connection", ip_address)
stdin, stdout, stderr = ssh_client.exec_command('ls -l')
stdout.read()
# print(stdout)
#remote_connection = ssh_client.invoke_shell()
#output = remote_connection.recv(50000)
# print(output)

# remote_connection.send
