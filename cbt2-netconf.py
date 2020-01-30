from ncclient import manager
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "172.16.7.200", "port": "22",
          "username": "admin", "password": "cisco"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
