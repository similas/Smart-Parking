#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time  # Can never get enough...

# ======================

MQTT_HOST = "broker.mqtt-dashboard.com"    # Server 
MQTT_PORT = 1883  # Port

# ======================


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    #Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("loopback/hello")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+": "+str(msg.payload))


def mqttPublish(sth):
    global client
    client.publish("EmbeddedProject/OpenDoor", payload=sth,
                qos=0, retain=False)
    

# =========================================

client = mqtt.Client(client_id="python-loopback")  # Create a client instance

# Callback declarations
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, 60) # Connect !

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()
index = 0

#===========================================

if __name__ == "__main__":
	while True:
	    # index = index + 1
	    publishString = input("What to publish ?  : ")
	    time.sleep(2)
	    # client.publish("EmbeddedProject/OpenDoor", payload=publishMqtt,
	    #                qos=0, retain=False)
	    mqttPublish(publishString)
	    print("Published ---> ", str(index))
                        