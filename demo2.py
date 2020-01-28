from ncclient import manager
from virl_router_info import router

config_template = open().read()


netconf_config  config_template.format(
    interface_name="GigabitEthernet1", interface_desc="GNS_Test")


# import logging
# logging.basicCconfig(level=logging.DEBUG)

# router = {"host": "172.16.7.241", "port": "830",
          "username": "admin", "password": "cisco"}
# print(router["host"])
# print(router["port"])
# print(router["username"])
# print(router["password"])

# netconf_filter = """
 # <filter>
 # <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
 #   <interface>
 #     <name>GigabitEthernet1</name>
 #   </interface>
 #  </interface>
 # </filter>
# """

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
#  for capability in m.server_capabilities:
#        print('*' * 50)
#        print(capability)
    # get the running config on the filtered out interface
    print('Connected')
    interface_netconf = m.get_config('running', netconf_filter)
    print('getting running config')
# below xml is a property of interface_conf

# XMLDOM for formatting output to xml
xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
print(xmlDom.toprettyxml(indent="  "))
print('*' * 25 + 'Break' + '*' * 50)
# XMLTODICT for formatting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]
# pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)
