import sys
import time
import grovepi
import json
import paho.mqtt.client as mqtt


# MQTT parameters
org='tjd6vv' # Replace this with the org id
host= org + '.messaging.internetofthings.ibmcloud.com'
clientid='d:'+ org +':Buttons:Button'
username='use-token-auth'
password='DEVICE_TOKEN' # Replace this with the device token of Button
topic = 'iot-2/evt/button/fmt/json'

# Sensor parameters
button = 3

client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
grovepi.pinMode(button,"INPUT")

while True:
    try:
        button_state=grovepi.digitalRead(button)

        if button_state == 1:
            payload={"Button" : "on"}
        else:
            payload={"Button" : "off"}
        client.publish(topic, json.dumps(payload))
        time.sleep(.5)
        print(button_state)
    except IOError:
        print ("Error")