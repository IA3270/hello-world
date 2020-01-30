#import ncclient
from ncclient import manager


#router = {"host": "172.16.7.241", "username": "admin", "password": "cisco"}


router = {"host": "172.16.7.241", "port": "22",
          "username": "admin", "password": "cisco"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    m.close_session()
# print(capability)


# with manager.connect(host=router["host"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
#    m.close_session()
