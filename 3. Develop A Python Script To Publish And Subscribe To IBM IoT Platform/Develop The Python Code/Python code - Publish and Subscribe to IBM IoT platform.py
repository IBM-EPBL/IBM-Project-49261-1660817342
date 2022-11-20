import time
import wiotp.sdk.device
import os
import datetime
import random
configure= {
"identity":{
"orgId": "wf4eku",
"typeId": "Devicel",
"deviceId": "DeviceID"},
"auth": {
"token": ") kAnd_XT+wy51fGnR7"
} }

clientDevice = wiotp.sdk.device.DeviceClient (config=configure, logHandlers=None)
clientDevice.connect()
def myCommandCallback (cmd) :
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command']) 
    m=cmd.data['command']
    if (m=="motoron"):
        print ("Motor is switched on")
    elif (m=="motoroff"):
        print ("Motor is switched OFF")
    print ("")
while True:
    soil=random.randint (0,100)
    temp=random.randint (-20, 125)
    hum=random.randint (0, 100)
    dataSet={'soil moisture': soil, 'temperature': temp, 'humidity':hum}
    clientDevice.publishEvent (eventId="status", msgFormat="json", data=dataSet, qos=0 ,onPublish=None)
    print ("Published data Successfully: %s", dataSet) 
    time.sleep (2)
clientDevice.commandCallback = myCommandCallback 
clientDevice.disconnect ()

