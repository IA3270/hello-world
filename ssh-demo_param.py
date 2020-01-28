import paramiko
import time
#from netmiko import ConnectHandler

ip_address = "172.16.7.241"
username = "admin"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print("Successful Connection", ip_address)

remote_connection = ssh_client.invoke_shell()
# print output

# remote_connection.send
