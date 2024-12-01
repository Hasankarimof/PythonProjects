import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 47.497913 # Your latitude
MY_LONG = 19.040236 # Your longitude
MY_EMAIL = "abdukarimovhasan4@gmail.com"
MY_PASSWORD = "fhtgspnkmnnozzwb"

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <=5:
        return True
    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    # Convert times to UTC
    sunrise_time = datetime.fromisoformat(sunrise)
    sunset_time = datetime.fromisoformat(sunset)
    current_time = datetime.utcnow()

    # If the current time is before sunrise or after sunset, it’s dark
    if current_time < sunrise_time or current_time > sunset_time:
        return True
    return False

# Step 4: Function to send email
def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is overhead and it’s dark. Go outside and look up!"
        )

# Step 5: Run the script every 60 seconds
while True:
    if is_iss_overhead() and is_dark():
        send_email()
    time.sleep(60)  # Wait for 60 seconds

