from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("cpx-switch/#") #declaring wildcard so that it will be accessible to all

def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    #this code will light up the pixel at index 0 if the msg.topic is equal to topic pub_switch
    if msg.topic == "cpx-switch/pub_switch":

        if msg.payload.decode() == "true":
            cp.pixels[0] = (255,255,255)
        else:
            cp.pixels[0] = (0,0,0) #off the light if the switch is set into false
 #this code will light up the pixel at index 1 if the msg.topic is equal to topic pub_switch2
    elif msg.topic == "cpx-switch/pub_switch2":

        if msg.payload.decode() == "true":
            cp.pixels[1] = (255,255,255)
        else:
            cp.pixels[1] = (0,0,0) #off the light if the switch is set into false
 #this code will light up the pixel at index 2 if the msg.topic is equal to topic pub_switch3
    elif msg.topic == "cpx-switch/pub_switch3":

        if msg.payload.decode() == "true":
            cp.pixels[2] = (255,255,255)
        else:
            cp.pixels[2] = (0,0,0) #off the light if the switch is set into false
        
            
    
cp.red_led = False 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("mqtt.eclipseprojects.io", 1883, 60) #create connection

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt