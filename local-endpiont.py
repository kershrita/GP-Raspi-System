import requests
import random
import time
import adafruit_dht
import board

API_URL = "http://192.168.1.45/graduation/public/api/sensor/readings"

# Initialize DHT22 sensor
sensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity

        # Create message JSON
        payload = {
            "readings": [
                {"sensor_id": 1, "value": humidity},
                {"sensor_id": 2, "value": temperature}
            ]
        }
        
        print("Sending message:", payload)
        requests.post(API_URL, json=payload)
        print("Message sent!")

    except RuntimeError as e:
        print("Error reading DHT22:", e)

    time.sleep(5)  # Send data every 10 seconds
