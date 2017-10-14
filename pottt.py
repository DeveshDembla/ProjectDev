import httplib2
import serial

ser = serial.Serial('/dev/ttyACM0')
ser.baudrate = 9600
temp = ' '
a = 0

while True:
	ch = ser.read(1)
	if ch=='\n':
		print temp
		a = int(temp)
		conn = httplib2.Http()	
		conn.request("https://api.thingspeak.com/update?api_key=HPPFQXUPOY4DML6N&field1=%d" %(a))
		temp = ' '
	else:
		temp+=ch	
