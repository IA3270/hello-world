import paramiko
import time
from netmiko import ConnectHandler

CSR1 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.7.241',
    'username': 'admin',
    'password': 'cisco',
}

net_connect = ConnectHandler(**CSR1)
# output = net_connect.send_command('show ip int brief', 'enable', 'cisco',)
#                                  'config t', 'int loop 1', 'ip address 1.1.1.1 255.255.255.255', 'ctrl z')
# print(output)

# config_commands = ['enable', 'cisco', 'config t',
#                   'int loop 20', 'ip address 1.1.1.1 255.255.255.255']
# output = net_connect.send_config_set(config_commands)
# print(output)

# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=ip_address, username=username,
#                   password=password)

# print("Successful Connection", ip_address)

# remote_connection = ssh_client.invoke_shell()

# net_connect = ConnectHandler(**CSR1)
output = net_connect.send_command('show ip int brief\n')
print(output)
#output2 = net_connect.send_command('enable\n', 'cisco\n', 'config t\n')
# remote_conn = remote_conn_pre.invoke__shell()
# output = remote_conn.recv(65535)
# print(output2)

#config_commands = ['enable\n', 'cisco\n', 'config t\n']
#config_commands = ['config t\n']
#output2 = net_connect.send_config_set(config_commands)
# print(output2)
# remote_conn.send("enable\n")
# remote_conn.send("cisco\n")
# remote_conn.send("config terminal\n")
# remote_conn.send("int loop10\n")
# remote_conn.send("ip address 10.10.10.1 255.255.255.255\n")
# remote_conn.send("end\n")
# remote_conn.send("exit\n")

# remote_connection.send("enable\n")
# remote_connection.send("config terminal\n")
# remote_connection.send("password\n")
# remote_connection.send("int loop10\n")
# remote_connection.send("ip address 10.10.10.1 255.255.255.255\n")
# remote_connection.send("router opsf 100\n")
# remote_connection.send("network 10.10.10.0 0.0.0.255 area0\n")
# remote_connection.send("end\n")

time.sleep(1)
# output = remote_connection.recv(65535)
# print output

# ssh_client.close

# remote_connection.send
