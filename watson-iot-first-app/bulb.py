import paho.mqtt.client as mqtt
import json
import grovepi

# MQTT parameters
org='tjd6vv' # Replace this with the org id
host= org + '.messaging.internetofthings.ibmcloud.com'
clientid='d:'+ org +':Bulbs:Bulb'
username='use-token-auth'
password='DEVICE_TOKEN' # Replace this with the device token of Bulb
topic = 'iot-2/cmd/state/fmt/json'

# Device parameters
led=3
button="off";


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):

    button= json.loads(msg.payload)["state"]
    if button == "on":
            grovepi.digitalWrite(led,1)
    else:
            grovepi.digitalWrite(led,0)
    print(button);

client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
client.subscribe(topic)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()