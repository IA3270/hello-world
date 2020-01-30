import paramiko
import time
from netmiko import ConnectHandler

# CSR1 = {
#    'device_type': 'cisco_ios',
#    'ip': '172.16.7.241',
#    'username': 'admin',
#    'password': 'cisco'
# }
ip_address = "172.16.7.241"
username = "admin"
password = "cisco"
enable = "enable"
en_pwd = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username,
                   password=password)

print("Successful Connection", ip_address)

remote_connection = ssh_client.invoke_shell()

# net_connect = ConnectHandler(**CSR1)
#output = net_connect.send_command('show ip int brief')
# print(output)
# remote_conn = remote_conn_pre.invoke__shell()
# output = remote_conn.recv(65535)
# print output

# remote_conn.send("enable\n")
# remote_conn.send("cisco\n")
# remote_conn.send("config terminal\n")
# remote_conn.send("int loop10\n")
# remote_conn.send("ip address 10.10.10.1 255.255.255.255\n")
# remote_conn.send("end\n")
# remote_conn.send("exit\n")

# remote_connection.send("enable\n")
remote_connection.send("ter len 0\n")
remote_connection.send("sh ip int brief\n")
#remote_connection.send("int loop80\n")
# remote_connection.send("exit\n")
#remote_connection.send("ip address 88.10.10.1 255.255.255.255\n")
#remote_connection.send("router ospf 100\n")
#remote_connection.send("network 90.10.10.0 0.0.0.255 area 0\n")
#remote_connection.send("network 88.10.10.0 0.0.0.255 area 0\n")
# remote_connection.send("end\n")
#remote_connection.send("wr mem\n")

#output = net_connect.send_command('show running config\n')
#remote_connection.send('ter len 0\n')
#remote_connection.send('show running config\n')
# print(output)
# remote_connection.send("wr mem\n")
# print(output)

time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close

# remote_connection.send
