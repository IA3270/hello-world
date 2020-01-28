import paramiko
#from netmiko import ConnectHandler
CSR = {
    'device-type': 'cisco_ios',
    'ip': '172.16.7.241',
    'username': 'admin',
    'password': 'cisco'
}
net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show ip int brief')
print(output)
