# Raspberry-PI-3-Blueetooth

The program consists in a bluetooth search, that find nearby devices and register then in a txt file.

To run the code, first you need to download de lib pybluez that have some functions we will use.

Open the terminal and write the following lines: 

**$ sudo apt-get install python-dev libbluetooth-dev**

**$ git clone https://github.com/karulis/pybluez.git**

**$ cd pybluez**

**$ sudo python setup.py install**

**$ sudo python3 setup.py install**

After install the lib, you will have to create the txt file bluetooth_devices.txt and write in terminal:

**$ python bluetooth_search.py**
