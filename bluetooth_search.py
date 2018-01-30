from bluetooth import bluez
import datetime
import time
while True:
    file_object = open("bluetooth_devices.txt","a")
    nearby_devices = bluez.discover_devices(lookup_names = True)
    for name, addr in nearby_devices:
        if nearby_devices is not None:
            print "{} : {}".format(datetime.datetime.now(),nearby_devices)
            file_object.write("{} : {} {}\n".format(datetime.datetime.now(),name,addr))
    file_object.close()
    time.sleep(10)
