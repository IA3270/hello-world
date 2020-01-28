from ncclient import manager
import netmiko


router = {"hosthame": "CSR1VK-1", "ip address": "172.16.7.241", "port": "22",
          "username": "admin", "password": "cisco", "enable": "cisco"}
print(router["host"])
print(router["port"])
print(router["username"])
print(router["password"])

with manager.connect(hostname=router["hostname"], ip_address=router["ip address"], port=router["port"], username=router["username"], password=router["password"], enable=router["enable"]
                     close.session)


print(" ")
