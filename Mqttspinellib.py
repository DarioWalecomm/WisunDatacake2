#!/usr/bin/env python3
from spynel-cli import
def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    # Subscribe here!
    client.subscribe("dtck-pub/gateway-1/f0965f63-44ea-4b87-a2fc-469c45841823/INSTRUCCION")
def on_message(client, userdata, msg):
    A = str(msg.payload)
    A = A[2:-1]
    print(A)
    
client = mqtt.Client("Scriptpc") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.tls_set()
client.username_pw_set("633ec0271cedc303b3dc90365ffe73525b590325", "633ec0271cedc303b3dc90365ffe73525b590325")
client.connect("mqtt.datacake.co", 8883, 60)
client.loop_forever()  # Start networking daemon




