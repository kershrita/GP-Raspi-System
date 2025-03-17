import time
import adafruit_dht
import board
from azure.iot.device import IoTHubDeviceClient, Message

# IoT Hub connection string
CONNECTION_STRING = ""

# Initialize IoT client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Initialize DHT22 sensor
sensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity

        # Create message JSON
        msg = Message(f'{{"temperature": {temperature:.2f}, "humidity": {humidity:.2f}}}')
        
        print("Sending message:", msg)
        client.send_message(msg)
        print("Message sent!")

    except RuntimeError as e:
        print("Error reading DHT22:", e)

    time.sleep(10)  # Send data every 10 seconds
