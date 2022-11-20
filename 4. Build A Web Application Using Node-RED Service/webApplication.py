def myCommandCallback (cmd) :
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    mes=cmd.data['command']
    if (mes=="motoron"):
        print ("Motor is switched on")
    elif (mes=="motoroff"):
        print ("Motor is switched OFF")
    print (" ")
while True:
    soil=random.randint (0,100)
    temp=random.randint (-20, 125)
    hum=random.randint (0, 100)
    dataSet={'soil moisture': soil, 'temperature':temp, 'humidity':hum}
    clientDevice.publishEvent (eventId="status", msgFormat="json", data=dataSet, qos=0 , onPublish=None)
    print ("Published data Successfully: %s", dataSet)
    time.sleep (2)
clientDevice.commandCallback = myCommandCallback
clientDevice.disconnect ()                   