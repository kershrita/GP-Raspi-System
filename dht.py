import adafruit_dht
import board
import time

sensor = adafruit_dht.DHT22(board.D4)

while True:
	try:
		temperature = sensor.temperature
		humidity = sensor.humidity
		print(f"Temperature: {temperature:.2f} C")
		print(f"Humidity: {humidity:.2f}%")
	except RuntimeError as e:
		print(f"Error reading DHT22: {e}")
	
	time.sleep(2)
