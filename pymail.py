import smtplib
import time
import RPi.GPIO as GPIO
import struct
from bluepy.btle import UUID, Peripheral

threshold = 10.05

fromaddr = 'frommachine105@gmail.com'
toaddrs  = 'toowner@gmail.com'
msg = 'I need immediate service and I wanted you to know!'

# Credentials (if needed)
username = 'username'
password = 'password'


service_uuid = UUID("1493dd8e-8c3e-4e74-a4ff-6f0cd50005f9")
char_vibr_uuid = UUID("1493dd8e-8c3e-4e78-a4ff-6f0cd50005f9")

v = Peripheral(sys.argv[1])
Testsevice=v.getServiceByUUID(service_uuid)
try:
    ch_vibr = Testsevice.getCharacteristics(char_vibr_uuid)[0]

    while 1:
        vibrVal = struct.unpack('<f', ch_temp.read())[0]
        # The actual mail send
        if vibrVal > threshold
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login(username,password)
			server.sendmail(fromaddr, toaddrs, msg)
			server.quit()
		elif
		    time.sleep(10);
finally:
	v.disconnect()

