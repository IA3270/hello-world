from ncclient import manager
from pprint import pprint
import xmltodict
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "172.16.7.200", "port": "22",
          "username": "admin", "password": "cisco"}


netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Ethernet1/1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Ethernet1/2</name>
    </interface>
  </interfaces-state>
</filter>
"""
with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

        interface_netconf = m.get_config(netconf_filter)
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent="  "))
        print('*' * 25 + 'Break' + '*' * 50)

        #print('getting running config')
    m.close_session()
# XMLTODICT for converting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]
pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)

config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']['#text']}")
print(f"Description: {config['description']}")
print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")
