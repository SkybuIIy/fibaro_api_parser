### imports ###
import datetime
import time
import io
import sys
import requests
import json
import configparser
import csv

### stuff ###
hcIP = "192.168.188.53"
login = input("e-mail: ")
password = input("password: ")
hc2auth = login, password
baseUrl = 'http://' + hcIP + '/api/'

### functions ###
# will make prettier and add functionalities
# from https://forum.fibaro.com/topic/50810-connecting-to-fibaro-api-python/
# need to do: cast json to csv format
def do_request(path, method="GET", params={}, headers={}):
        if method == "GET":
            response = requests.get(path, headers=headers, auth=hc2auth)
        elif method == "POST":
            headers["Content-Type"] = "application/json"
            response = requests.post(
                path,
                data=json.dumps(params),
                headers=headers,
                 auth=hc2auth)
        elif method == "PUT":
            headers["Content-Type"] = "application/json"
            response = requests.put(
                path,
                data=json.dumps(params),
                headers=headers,
                 auth=hc2auth)
        elif method == "DELETE":
            response = requests.delete(
                path,
                data=json.dumps(params),
                headers=headers,
                auth=hc2auth)
        return response.json()

# add conversion from "normal" time to unix epoch and vice versa

# possible paths/queries:
### NOT TESTED YET ###
# right now still in json format, will try to cast soon
# make one function that gets all
# make function that prints all functionalities --help

### these functions still need adjustments ###
# settings
# general settings - URL: /api/settings/info
def get_general_settings(hcIP):
    response = requests.get("http://"+hcIP+"/api/settings/info", auth=hc2auth)
    return response.json()

# backups - URL: /api/settings/backups
def get_backups(hcIP):
    response = requests.get("http://"+hcIP+"/api/settings/backups", auth=hc2auth)
    return response.json()

# location - URL: /api/settings/location
def get_location(hcIP):
    response = requests.get("http://"+hcIP+"/api/settings/locations", auth=hc2auth)
    return response.json()

# network settings - URL: /api/settings/network
def get_network_settings(hcIP):
    response = requests.get("http://"+hcIP+"/api/settings/network", auth=hc2auth)
    return response.json()

# general
# devices - URL: /api/devices
def get_devices(hcIP):
    response = requests.get("http://"+hcIP+"/api/devices", auth=hc2auth)
    return response.json()

# sections - URL: /api/sections
def get_sections(hcIP):
    response = requests.get("http://"+hcIP+"/api/sections", auth=hc2auth)
    return response.json()

# rooms - URL: /api/rooms
def get_rooms(hcIP):
    response = requests.get("http://"+hcIP+"/api/rooms", auth=hc2auth)
    return response.json()

# scenes - URL: /api/scenes
def get_scenes(hcIP):
    response = requests.get("http://"+hcIP+"/api/scenes", auth=hc2auth)
    return response.json()

# users - URL: /api/users
def get_devices(hcIP):
    response = requests.get("http://"+hcIP+"/api/devices", auth=hc2auth)
    return response.json()

# global variables - URL: /api/globalVariables 
def get_global_varaibles(hcIP):
    response = requests.get("http://"+hcIP+"/api/globalVariables", auth=hc2auth)
    return response.json()

# rgb programs - URL: /api/RGBPrograms
def get_rgb_programs(hcIP):
    response = requests.get("http://"+hcIP+"/api/RGBPrograms", auth=hc2auth)
    return response.json()

# tracking schedules - URL: /api/trackingSchedules
def get_tracking_schedules(hcIP):
    response = requests.get("http://"+hcIP+"/api/trackingSchedules", auth=hc2auth)
    return response.json()

# linked devices - URL: /api/linkedDevices
def get_linked_devices(hcIP):
    response = requests.get("http://"+hcIP+"/linkedDevices", auth=hc2auth)
    return response.json()

# virtual devices - URL: /api/virtualDevices
def get_virtual_devices(hcIP):
    response = requests.get("http://"+hcIP+"/api/virtualDevices", auth=hc2auth)
    return response.json()

# iOS devices - URL: /api/iosDevices
def get_ios_devices(hcIP):
    response = requests.get("http://"+hcIP+"/api/iosDevices", auth=hc2auth)
    return response.json()

# voip devices - URL: /api/voip
def get_voip_devices(hcIP):
    response = requests.get("http://"+hcIP+"/api/voip", auth=hc2auth)
    return response.json()

# icons - URL: /api/icons
def get_icons(hcIP):
    response = requests.get("http://"+hcIP+"/api/icons", auth=hc2auth)
    return response.json()

# panels
# sms notifications - URL: /api/panels/sms
def get_panel_sms_notifs(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/sms", auth=hc2auth)
    return response.json()

# location - URL: /api/panels/location
def get_panel_location(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/location", auth=hc2auth)
    return response.json()

# history panel - URL: /api/panels/history
def get_panel_history(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/history", auth=hc2auth)
    return response.json()

# notifications panel - URL: /api/panels/notifications
def get_panel_notifs(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/notifications", auth=hc2auth)
    return response.json()

# heating panel - URL: /api/panels/heating
def get_panel_heating(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/heating", auth=hc2auth)
    return response.json()

# AC panel - URL: /api/panels/cooling
def get_panel_ac(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/cooling", auth=hc2auth)
    return response.json()

# humidity panel - URL: /api/panels/humidity
def get_panel_humidity(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/humidity", auth=hc2auth)
    return response.json()

# alarm panel - URL: /api/panels/alarm
def get_panel_alarm(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/alarm", auth=hc2auth)
    return response.json()

# drenchers panel - URL: /api/panels/drenchers
def get_panel_drenchers(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/drenchers", auth=hc2auth)
    return response.json()

# favorite colors - URL: /api/panels/favoriteColors
def get_panel_fav_colors(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/favoriteColors", auth=hc2auth)
    return response.json()

# fibaro alarm panel - URL: /api/panels/fibaroAlarm
def get_panel_fibaro_alarm(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/fibaroAlarm", auth=hc2auth)
    return response.json()

# energy panel - URL: /api/panels/energy
def get_panel_energy(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/energy", auth=hc2auth)
    return response.json()

# temperature panel - URL: /api/panels/temperature
def get_panel_temperature(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/temperature", auth=hc2auth)
    return response.json()

# events panel - URL: /api/panels/event
def get_panel_events(hcIP):
    response = requests.get("http://"+hcIP+"/api/panels/event", auth=hc2auth)
    return response.json()

# plugins
# plugins types - URL: /api/plugins/types
def get_plugins_types(hcIP):
    response = requests.get("http://"+hcIP+"/api/plugins/types", auth=hc2auth)
    return response.json()

# plugins installed - URL: /api/plugins/installed
def get_plugins_installed(hcIP):
    response = requests.get("http://"+hcIP+"/api/plugins/installed", auth=hc2auth)
    return response.json()

# other
# login status - URL: /api/loginStatus
def get_login_status(hcIP):
    response = requests.get("http://"+hcIP+"/api/loginStatus", auth=hc2auth)
    return response.json()

# password reminder - URL: /api/passwordForgotten
def get_password_reminder(hcIP):
    response = requests.get("http://"+hcIP+"/api/passwordForgotten", auth=hc2auth)
    return response.json()

# refresh states - URL: /api/refreshStates
def get_refresh_states(hcIP):
    response = requests.get("http://"+hcIP+"/api/refreshStates", auth=hc2auth)
    return response.json()

# network discovery - URL: /api/networkDiscovery/arp
def get_network_discovery(hcIP):
    response = requests.get("http://"+hcIP+"/api/networkDiscovery", auth=hc2auth)
    return response.json()

# get everything
#def get_everything(hcIP):
    # how to do this best? append to json? or convert to csv right away?
    #get_general_settings(hcIP)

# convert json to csv
def json_to_csv(jsondata):
    csv_file = open(input("full path for csv file: "), 'w', newline='')
    csv_writer = csv.writer(csv_file)
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    csv_file.close()

# sample request for all events between certain times
# will later add that user can input ip and timeframe/device id/etc
#print(do_request("http://192.168.188.53/api/panels/event?from=1647978548&to=1648064948", ))

json_to_csv(do_request("http://192.168.188.53/api/panels/event?from=1647978548&to=1648064948", ))
