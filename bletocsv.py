import os
import time 
from time import sleep
import sys
import binascii
import struct
from bluepy.btle import UUID, Peripheral
import datetime
import logging


service_uuid = UUID("1493dd8e-8c3e-4e74-a4ff-6f0cd50005f9")
char_temp_uuid = UUID("1493dd8e-8c3e-4e76-a4ff-6f0cd50005f9")
char_humid_uuid = UUID("1493dd8e-8c3e-4e77-a4ff-6f0cd50005f9")
char_vibr_uuid = UUID("1493dd8e-8c3e-4e78-a4ff-6f0cd50005f9")
char_alight_uuid = UUID("1493dd8e-8c3e-4e79-a4ff-6f0cd50005f9")
char_aq_uuid = UUID("1493dd8e-8c3e-4e75-a4ff-6f0cd50005f9")

TestService=p.getServiceByUUID(service_uuid)
try:
    ch_temp = TestService.getCharacteristics(char_temp_uuid)[0]
    ch_humid = TestService.getCharacteristics(char_humid_uuid)[0]
    ch_vibr = TestService.getCharacteristics(char_vibr_uuid)[0]
    ch_alight = TestService.getCharacteristics(char_alight_uuid)[0]
    ch_aq = TestService.getCharacteristics(char_aq_uuid)[0]

        

file = open("/home/pi/data_log.csv", "a")
i=0
if os.stat("/home/pi/data_log.csv").st_size == 0:
        file.write("Time,Temperature,Humidity,Vibration,Ambient Light,Air Quality\n")
while True:
        

        tempVal = struct.unpack('<f', ch_temp.read())[0]
        humidVal = struct.unpack('<f', ch_humid.read())[0]
        vibrVal = struct.unpack('<f', ch_vibr.read())[0]
        alightVal = struct.unpack('<f', ch_alight.read())[0]
        aqVal = struct.unpack('<f', ch_aq.read())[0]
        now = datetime.now()
        file.write(str(now)+","+str(tempVal)+","+str(humidVal)+","+str(vibrVal)+","+str(alightVal)+","+str(aqVal)+"\n")
        file.flush()
        time.sleep(5)<br>file.close()