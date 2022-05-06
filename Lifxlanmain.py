import lifxlan
import sys
import paho.mqtt.client as mqtt
import logging
import json
from lifxlan import BLUE, COLD_WHITE, CYAN, GOLD, GREEN, LifxLAN, \
    ORANGE, PINK, PURPLE, RED, WARM_WHITE, WHITE, YELLOW
import time
####################### Lifx light functions #####################################################
def set_red(light):
    light.set_color(RED,0,True)
def set_blue(light):
    light.set_color(BLUE,0,True)
def set_green(light):
    light.set_color(GREEN,0,True)
def set_yellow(light):
    light.set_color(YELLOW,0,True)
def set_white(light):
    light.set_color(WHITE,0,True)
def turn_off_device(light):
    light.set_power('off',0,True)
def turn_on_device(light):
    light.set_power('on',0,True)

######################### MQTT functions ######################################################
def on_connect(client, userdata, flags, rc):
    logging.debug("Connected with result code "+str(rc))
    client.subscribe("looplocal/loopobjectevent/bcbada00-7a40-4f49-8b60-a1beb5b30031/+/trackedPlace")
    # client.subscribe("looplocal/loopobjectevent/bcbada00-7a40-4f49-8b60-a1beb5b30031/e76fe464-3b53-4938-9fab-9868278539ac/trackedPlace")
    # client.subscribe("looplocal/loopobjectevent/bcbada00-7a40-4f49-8b60-a1beb5b30031/4b1aa5c1-7263-4969-8e1b-089adf5e276d/trackedPlace")
    
def on_disconnect(client, userdata,rc=0):
    logging.debug("Disconnected result code "+str(rc))
    client.loop_stop()

def on_message(client,userdata,msg): 
    msg_dict = json.loads(msg.payload.decode('utf-8'))    #convert to dict
    place_id = msg_dict.get('trackedPlace').get('value')
    tag_MAC = msg_dict.get('description')
    placeinproperlist(tag_MAC,place_id)
    #volume_based_colour(tag_MAC,place_id)
    #tag_based_colour(tag_MAC,place_id)
####################### Logic functions ####################################################
def placeinproperlist(tag_id,place_id):
    global mainoffice,lab,small_component_room,warehouse,callroom
    indexed_list = listoplaces[:int(listoplaces.index(place_id))] + listoplaces[int(listoplaces.index(place_id))+1:]
    zone = place_id_dict.get(place_id)
    if tag_id not in zone:
        zone.append(tag_id)
        for i in indexed_list:
                if tag_id in place_id_dict.get(i):
                    place_id_dict.get(i).remove(tag_id)

def volume_colourtags(light:str,taglen: int):
    if taglen ==0:
        turn_off_device(light)
        return
    elif 0 < taglen <= 1:
        turn_on_device(light)
        set_blue(light)
        return
    elif  taglen > 1:
        turn_on_device(light)
        set_red(light)
        return

def cycle_tag_colours(light,taglist):
    i = 0
    if len(taglist) == 0:
        turn_off_device(light)
    elif len(taglist) == 1:
        turn_on_device(light)
        for tagmac in taglist:
            try:
                tagcolor = tag_colours_dict[tagmac]
                light.set_color(tagcolor,0,True)
            except:
                print("tag listed not tracked")
            pass
    elif len(taglist) > 1:
            for tagmac in taglist:
                    tagcolor = tag_colours_dict[tagmac]
                    light.set_color(tagcolor,0,True)
                    time.sleep(1.5)

####################################################################################################
zoneLight1 = lifxlan.Light("d0:73:d5:68:96:da", "192.168.9.184")
zoneLight2  = lifxlan.Light("d0:73:d5:68:74:fe", "192.168.9.147")

mainoffice = []
lab =[]
small_component_room = []
warehouse = []
callroom =[]
conference =[]
mainofficecubicles = []
none_place = []

place_id_dict = {
     '61b87122-6b74-485e-a1b6-a10f91eeddde' : mainoffice,
     'cf4e1d26-1609-43da-9cf8-758d1b18fa3b' : lab,
     'ac5a3913-c1ce-459e-863e-02cc860eedff' : small_component_room,
     '36ffc47b-b315-4d42-ba7d-4794a215295d': callroom,
     '1b02863e-97fe-476c-82ae-6908281cea73' : warehouse,
     'fa9a6eba-10f9-4cef-9e5b-52f3b76b7f87' : conference,
     '4f69a634-9504-4908-b857-ccc2d4ee0ad8' : mainofficecubicles,
     '8ca74615-265f-4734-9579-0f9cdb2dba5c' : none_place
    }
    
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

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.20.99",1883,0)
client.loop_start()
while 1:
    light_volumeoftags = {
    zoneLight1 : mainoffice,
    #  'lightid2' : len(lab),
    #  'lightid3' : len(small_component_room),
    #  'lightid4' : len(callroom),
    zoneLight2 :mainofficecubicles, 
      }
    alllights = list(light_volumeoftags.keys())
    for light in alllights:
        try:
            cycle_tag_colours(light,light_volumeoftags[light])
            #volume_colourtags(light,len(light_volumeoftags[light]))
            print([light,light_volumeoftags[light]])
        except:
            print("tag does not exist")
            pass
client.loop_stop()