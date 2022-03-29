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
hc2auth = "login", "password"
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
# general settings - URL: /api/settings/info
# backups - URL: /api/settings/backups
# location - URL: /api/settings/location
# network settings - URL: /api/settings/network
# devices - URL: /api/devices
# sections - URL: /api/sections
# rooms - URL: /api/rooms
# scenes - URL: /api/scenes
# users - URL: /api/users
# global variables - URL: /api/globalVariables 
# rgb programs - URL: /api/RGBPrograms
# tracking schedules - URL: /api/trackingSchedules
# linked devices - URL: /api/linkedDevices
# virtual devices - URL: /api/virtualDevices
# iOS devices - URL: /api/iosDevices
# voip devices - URL: /api/voip
# icons - URL: /api/icons
# panels
# sms notifications - URL: /api/panels/sms
# location - URL: /api/panels/location
# history panel - URL: /api/panels/history
# notifications panel - URL: /api/panels/notifications
# heating panel - URL: /api/panels/heating
# AC panel - URL: /api/panels/cooling
# humidity panel - URL: /api/panels/humidity
# alarm panel - URL: /api/panels/alarm
# drenchers panel - URL: /api/panels/drenchers
# favorite coloros - URL: /api/panels/favoriteColors
# fibaro alarm panel - URL: /api/panels/fibaroAlarm
# energy panel - URL: /api/panels/energy
# temperature panel - URL: /api/panels/temperature
# events panel - URL: /api/panels/event
# plugins
# plugins types - URL: /api/plugins/types
# plugins installed - URL: /api/plugins/installed
# other
# login status - URL: /api/loginStatus
# password reminder - URL: /api/passwordForgotten
# refresh states - URL: /api/refreshStates
# network discovery - URL: /api/networkDiscovery/arp

# sample request for all events between certain times
# will later add that user can input ip and timeframe/device id/etc
print(do_request("http://192.168.188.53/api/panels/event?from=1647978548&to=1648064948", ))