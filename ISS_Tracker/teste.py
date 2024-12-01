import requests
from datetime import datetime
#
#
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
#
# # Response Codes 404 = Doesnt exist
# # 1XX : Hold on
# # 2XX: Here you Go
# # 3XX: Go Away
# # 4XX: You Screwed Up
# # 5XX: I Screwed Up server is not working

parameters = {
    "lat":"47.497913",
    "lng":"19.040236",
    "formatted":0,
}



response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunset.split("T")[1].split(":")[0])
print(sunrise.split("T")[1].split(":")[0])


time_now = datetime.now()
print(time_now.hour)

