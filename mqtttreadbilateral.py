# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:35:24 2023
@author: Dario
"""
import threading
import time
import paho.mqtt.client as mqtt
UARTSENT = "/dev/ttyS5" 
broker="mqtt.datacake.co"
DATACAKE_TOKEN = "633ec0271cedc303b3dc90365ffe73525b590325"
port=8883
def on_connect(client, userdata, flags, rc):
    print("CONNECTED")
    print("Connected with result code: ", str(rc))
    client.subscribe("dtck-pub/gateway-1/f0965f63-44ea-4b87-a2fc-469c45841823/INSTRUCCION")
def on_message(client, userdata, message):
    A = str(message.payload)
    A = A[2:-1]
    print(A)
def main():
    print("WAIT for max: ",2)
    while True:
        time.sleep(1000)
        client.publish("dtck-pub/gateway-1/f0965f63-44ea-4b87-a2fc-469c45841823/LITORS_STRING","dfdfd")
### MQTT ###
client = mqtt.Client()
client.connect(broker, port)
client.on_connect = on_connect
client.tls_set()
client.username_pw_set("633ec0271cedc303b3dc90365ffe73525b590325", "633ec0271cedc303b3dc90365ffe73525b590325")
client.connect("mqtt.datacake.co", 8883, 60)
#client.on_disconnect = on_disconnect
def subscribing():
    client.on_message = on_message
    client.loop_forever()
sub=threading.Thread(target=subscribing)
pub=threading.Thread(target=main)
### Start MAIN ###
sub.start()
pub.start()