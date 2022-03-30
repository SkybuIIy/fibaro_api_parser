### imports ###
import datetime
import time
import io
import sys
import requests
import json
import configparser

### stuff ###
hc2IP = "192.168.188.53"
login = input("e-mail: ")
password = input("password: ")
hc2auth = login, password
baseUrl = 'http://' + hc2IP + '/api/'

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
# make on function that gets all
# make function that prints all functionalities --help

# general settings - URL: /api/settings/info
def get_general_settings(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/settings/info", auth=hc2auth)
    return response.json()

# backups - URL: /api/settings/backups
def get_backups(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/settings/backups", auth=hc2auth)
    return response.json()

# location - URL: /api/settings/location
def get_location(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/settings/locations", auth=hc2auth)
    return response.json()

# network settings - URL: /api/settings/network
def get_network_settings(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/settings/network", auth=hc2auth)
    return response.json()

# devices - URL: /api/devices
def get_devices(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/devices", auth=hc2auth)
    return response.json()

# sections - URL: /api/sections
def get_sections(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/sections", auth=hc2auth)
    return response.json()

# rooms - URL: /api/rooms
def get_rooms(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/rooms", auth=hc2auth)
    return response.json()

# scenes - URL: /api/scenes
def get_scenes(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/scenes", auth=hc2auth)
    return response.json()

# users - URL: /api/users
def get_devices(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/devices", auth=hc2auth)
    return response.json()

# global variables - URL: /api/globalVariables 
def get_global_varaibles(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/globalVariables", auth=hc2auth)
    return response.json()

# rgb programs - URL: /api/RGBPrograms
def get_rgb_programs(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/RGBPrograms", auth=hc2auth)
    return response.json()

# tracking schedules - URL: /api/trackingSchedules
def get_tracking_schedules(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/trackingSchedules", auth=hc2auth)
    return response.json()

# linked devices - URL: /api/linkedDevices
def get_linked_devices(hc2IP):
    response = requests.get("http://"+hc2IP+"/linkedDevices", auth=hc2auth)
    return response.json()

# virtual devices - URL: /api/virtualDevices
def get_virtual_devices(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/virtualDevices", auth=hc2auth)
    return response.json()

# iOS devices - URL: /api/iosDevices
def get_ios_devices(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/iosDevices", auth=hc2auth)
    return response.json()

# voip devices - URL: /api/voip
def get_voip_devices(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/voip", auth=hc2auth)
    return response.json()

# icons - URL: /api/icons
def get_icons(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/icons", auth=hc2auth)
    return response.json()

# panels
# sms notifications - URL: /api/panels/sms
def get_panel_sms_notifs(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/sms", auth=hc2auth)
    return response.json()

# location - URL: /api/panels/location
def get_panel_location(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/location", auth=hc2auth)
    return response.json()

# history panel - URL: /api/panels/history
def get_panel_history(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/history", auth=hc2auth)
    return response.json()

# notifications panel - URL: /api/panels/notifications
def get_panel_notifs(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/notifications", auth=hc2auth)
    return response.json()

# heating panel - URL: /api/panels/heating
def get_panel_heating(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/heating", auth=hc2auth)
    return response.json()

# AC panel - URL: /api/panels/cooling
def get_panel_ac(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/cooling", auth=hc2auth)
    return response.json()

# humidity panel - URL: /api/panels/humidity
def get_panel_humidity(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/humidity", auth=hc2auth)
    return response.json()

# alarm panel - URL: /api/panels/alarm
def get_panel_alarm(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/alarm", auth=hc2auth)
    return response.json()

# drenchers panel - URL: /api/panels/drenchers
def get_panel_drenchers(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/drenchers", auth=hc2auth)
    return response.json()

# favorite coloros - URL: /api/panels/favoriteColors
def get_panel_fav_colors(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/favoriteColors", auth=hc2auth)
    return response.json()

# fibaro alarm panel - URL: /api/panels/fibaroAlarm
def get_panel_fibaro_alarm(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/fibaroAlarm", auth=hc2auth)
    return response.json()

# energy panel - URL: /api/panels/energy
def get_panel_energy(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/energy", auth=hc2auth)
    return response.json()

# temperature panel - URL: /api/panels/temperature
def get_panel_temperature(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/temperature", auth=hc2auth)
    return response.json()

# events panel - URL: /api/panels/event
def get_panel_events(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/panels/event", auth=hc2auth)
    return response.json()

# plugins
# plugins types - URL: /api/plugins/types
def get_plugins_types(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/plugins/types", auth=hc2auth)
    return response.json()

# plugins installed - URL: /api/plugins/installed
def get_plugins_installed(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/plugins/installed", auth=hc2auth)
    return response.json()

# other
# login status - URL: /api/loginStatus
def get_login_status(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/loginStatus", auth=hc2auth)
    return response.json()

# password reminder - URL: /api/passwordForgotten
def get_password_reminder(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/passwordForgotten", auth=hc2auth)
    return response.json()

# refresh states - URL: /api/refreshStates
def get_refresh_states(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/refreshStates", auth=hc2auth)
    return response.json()

# network discovery - URL: /api/networkDiscovery/arp
def get_network_discovery(hc2IP):
    response = requests.get("http://"+hc2IP+"/api/networkDiscovery", auth=hc2auth)
    return response.json()


# sample request for all events between certain times
# will later add that user can input ip and timeframe/device id/etc
print(do_request("http://192.168.188.53/api/panels/event?from=1647978548&to=1648064948", ))
