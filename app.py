import paho.mqtt.client as mqtt

"""
Based on: 
https://pypi.org/project/paho-mqtt/

Interfacing with mqtt:
http://mqtt-explorer.com/
"""


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("mittaus/get")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f'{msg.topic}: {str(msg.payload.decode("utf-8"))}')

    # This is how to publish messages with python paho mqtt
    client.publish("mittaus/python", "message received")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.200", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
