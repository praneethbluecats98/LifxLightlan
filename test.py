from lifxlan import *
from time import sleep

lan = LifxLAN()
bulbs = lan.get_lights()
while(True):
    for bulb in bulbs:
        try:
            label = bulb.get_label()
            color = None
            if bulb.supports_multizone():
                color = bulb.get_color_zones()
            elif bulb.supports_color():
                color = bulb.get_color()
            else:
                color = "Color not supported"
            power = bulb.get_power()
            uptime = bulb.get_uptime()
            print("{} {} {} {}".format(label, color, power, uptime))
        except WorkflowException as e:
            print(e)
    sleep(2)



# # def volume_based_colour(tagmac,placeid):
# #     placeinproperlist(tagmac,placeid)
# #     light_volumeoftags = {
# #        zoneLight1 : len(mainoffice),
# #      #  'lightid2' : len(lab),
# #      #  'lightid3' : len(small_component_room),
# #      #  'lightid4' : len(callroom),
# #        zoneLight2 : len(mainofficecubicles), 
# #       }
# #     allights = list(lights_placesdict.values())
# #     for light in allights:
# #         tag_volume = light_volumeoftags.get(light)
# #         volume_colourlogic(light,tag_volume)

# def tag_based_colour(tagmac,placeid):
#     zonelight = lights_placesdict[placeid]
#     tagcolour =  tag_colours_dict[tagmac]
#     turn_on_device(zonelight)
#     zonelight.set_color(tagcolour,0,True)
#     time.sleep(0.5)
#     # placeinproperlist(tagmac,placeid)
#     # light_taglist = {
#     #    zoneLight1 : mainoffice,
#     #  #  'lightid2' : len(lab),
#     #  #  'lightid3' : len(small_component_room),
#     #  #  'lightid4' : len(callroom),
#     #    zoneLight2 : mainofficecubicles, 
#     #   }
#     # allights = list(lights_placesdict.values())
#     # for light in allights:
#     #     tag_list = light_taglist.get(light)
#     #     cycle_tag_colours(light,tag_list)


    
    # try:
    #     zonelight = lights_placesdict[placeid]
    #     lights = list(light_taglist.keys())
    #     for light in lights:
    #         if light_taglist[light] == 0:
    #             light.set_power("off")

    # except:
    #     print("place id has no associated light")
    #     pass
    # try:
    #     zonelight.set_power("on")
    #     zonelight.set_color(tagcolor)
    #     time.sleep(0.25)
        
    #     #print("i")
    # except:
    #     print("unable to set light colour")
    #     pass


    # Colors 
# colors = {
#     "red": RED, 
#     "orange": ORANGE, 
#     "yellow": YELLOW, 
#     "green": GREEN, 
#     "cyan": CYAN, 
#     "blue": BLUE, 
#     "purple": PURPLE, 
#     "pink": PINK, 
#     "white": WHITE, 
#     "cold_white": COLD_WHITE, 
#     "warm_white": WARM_WHITE, 
#     "gold": GOLD
# }
