###################################################################
#                Written by Hayden Taylor, 8/7/2018               #
###################################################################


'''

This program connects to OpenWeatherMap's API, and displays the name, weather, temperature, and humidity of a given city.

You can find a link to OWM's API here: https://openweathermap.org

You will need to generate your own API key, which you can put in the apiKey variable below.


Have fun!

'''


########################
#     DO NOT EDIT      # 
########################
import requests
import json
import time
import math
import urllib.parse
########################
########################



# SAMPLE KEY, this key will not work as it has been deactivated
apiKey = 'df452443b52dabf2b8ee362f5e9382b9' # INPUT YOUR OWN API KEY HERE



# DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
###################################################################

print('Enter "quit" or "q" to exit the program\n')

while True:


    city = input('City: ')
    print()

    if city == 'quit' or city == 'q':
        break


    url = 'https://api.openweathermap.org/data/2.5/weather?' + urllib.parse.urlencode({'q':city}) + ',us&appid=' + apiKey
    r = requests.get(url)
    jresponse = json.loads(r.text)

    name = jresponse['name']
    weather = jresponse["weather"][0]["description"]
    temperature = jresponse["main"]["temp"]

    faTemp = math.floor(1.8 * (temperature - 273) + 32)

    humidity = float(jresponse["main"]["humidity"])

    print('{}\'s weather consists of: {}, the temperature is {}°, and the humidity is {}%\n'.format(name,weather,faTemp,humidity))
