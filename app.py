import requests
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_location():
    location_url = 'http://www.geoplugin.net/json.gp'
    return requests.get(location_url).json()

location = get_location()

coords = {
    'lat': location['geoplugin_latitude'],
    'lng': location['geoplugin_longitude'],
}

def get_sunrise():
    sunrise_url = 'https://api.sunrise-sunset.org/json'
    return requests.get(sunrise_url, params=coords).json()

sunrise_res = get_sunrise()['results']

times = {
    'sunrise': sunrise_res['sunrise'],
    'sunset': sunrise_res['sunset']
}

print(times)
