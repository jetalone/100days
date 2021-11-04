import requests

MYLAT = 33.447750
MYLNG = -84.455130

parameters = {
    "lat": MYLAT,
    "lng": MYLNG
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)