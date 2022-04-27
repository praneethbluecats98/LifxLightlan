import lifxlan
import sys
import paho.mqtt.client as mqtt
import logging
import json
from lifxlan import BLUE, COLD_WHITE, CYAN, GOLD, GREEN,RED
class loop_zone:
    def __init__(self,zonelight,placeid,placelist):
        self.placelist = placelist
        self.placeid = placeid
        self.zonelight = zonelight

zoneLight1 = lifxlan.Light("d0:73:d5:68:96:da", "192.168.9.184")
zoneLight2  = lifxlan.Light("d0:73:d5:68:74:fe", "192.168.9.147")


# place_id_dict = {
#      '61b87122-6b74-485e-a1b6-a10f91eeddde' : mainoffice,
#      'cf4e1d26-1609-43da-9cf8-758d1b18fa3b' : lab,
#      'ac5a3913-c1ce-459e-863e-02cc860eedff' : small_component_room,
#      '36ffc47b-b315-4d42-ba7d-4794a215295d': callroom,
#      '1b02863e-97fe-476c-82ae-6908281cea73' : warehouse,
#      'fa9a6eba-10f9-4cef-9e5b-52f3b76b7f87' : conference,
#      '4f69a634-9504-4908-b857-ccc2d4ee0ad8' : mainofficecubicles,
#      '8ca74615-265f-4734-9579-0f9cdb2dba5c' : none_place
#     }
    
listoplaces = ['61b87122-6b74-485e-a1b6-a10f91eeddde','cf4e1d26-1609-43da-9cf8-758d1b18fa3b','ac5a3913-c1ce-459e-863e-02cc860eedff','1b02863e-97fe-476c-82ae-6908281cea73','36ffc47b-b315-4d42-ba7d-4794a215295d','fa9a6eba-10f9-4cef-9e5b-52f3b76b7f87','4f69a634-9504-4908-b857-ccc2d4ee0ad8','8ca74615-265f-4734-9579-0f9cdb2dba5c']

tag_colours_dict = {
    '31004224' : GREEN,
    '31004254' : BLUE,
    '3100425A' : RED,
    }

lights_placesdict = {
    '61b87122-6b74-485e-a1b6-a10f91eeddde':zoneLight1,
    #  'lightid2' : len(lab),
    #  'lightid3' : len(small_component_room),
    #  'lightid4' : len(callroom),
    '4f69a634-9504-4908-b857-ccc2d4ee0ad8':zoneLight2,
}
tagmac = '3100425A'

mainoffice = loop_zone(zoneLight1,'61b87122-6b74-485e-a1b6-a10f91eeddde',[])
warehouse = loop_zone(zoneLight2,'4f69a634-9504-4908-b857-ccc2d4ee0ad8',[])

warehouse.placelist.append(tagmac)
print(mainoffice.placeid)
print(warehouse.placelist)
#try:
print(mainoffice.zonelight)
#except:
#    pass
print(warehouse.placeid)

