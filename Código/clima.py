#! /usr/bin/python
import urllib2
import json
import time

#f = urllib2.urlopen('http://api.wunderground.com/api/e7d949410a7481dc/forecast10day/lang:SP$
#json_string = f.read()
#parsed_json = json.loads(json_string)

def lluvia(lat, lon):
        f = urllib2.urlopen('http://api.wunderground.com/api/e7d949410a7481dc/forecast10day/lang:SP/q/'+ str(lat) +','+ str(lon)  +'.json')
        json_string = f.read()
        parsed_json = json.loads(json_string)
        location = parsed_json['forecast']['txt_forecast']['forecastday'][0]['title']
        temp_c = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric']
        pop = parsed_json['forecast']['txt_forecast']['forecastday'][0]['pop']
        f.close()
        return pop