import ibmiotf.application
import time
import json

options = {
"org": "tjd6vv",
"id": "app1",
"auth-method": "apikey",
"auth-key": "AUTH_KEY", # Replace this with your auth key
"auth-token": "AUTH_TOKEN", # Replace this with your auth token
"clean-session": True
}

sourceDeviceType="Buttons"
sourceDeviceId="Button"
sourceEvent="button"

targetDeviceType="Bulbs"
targetDeviceId="Bulb"

def ButtonCallback(event):
	print "Got event " + json.dumps(event.data)
	button= event.data['Button']
	commandData={'state' : button }
	client.publishCommand(targetDeviceType, targetDeviceId, "state", "json", commandData)


client = ibmiotf.application.Client(options)

client.connect()
client.deviceEventCallback = ButtonCallback

client.subscribeToDeviceEvents(deviceType=sourceDeviceType, deviceId=sourceDeviceId, event=sourceEvent)

while True:
		time.sleep(1)