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

# sample request for all events between certain times
print(do_request("http://192.168.188.53/api/panels/event?from=1647978548&to=1648064948", ))