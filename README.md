# Uploading Sensor data to cloud

This project is based on sending sensor data to Thingspeak platform. Thingspeak platform is an IOT analytics platform by Mathworks

For simplicity, i have used a potentiometer in place of a sensor. It serves the purpose as we can change the resistance and see the realtime effect on Thingspeak

We have connected a potentiometer to an Arduino UNO board and using Python as the middleware, we are sending the data to Thingspeak. The python and Arduino codes have been uploaded.

For different sensors, the Arduino code would change(obviously) but the Python code should remain more or less the same.

httplib2 and serial libraries have been used for the python code.

The applications could be endless. For eg: A humidity sensor transmitting data would allow the owner to know that his plants are being watered properly. An ultrasonic / infrared sensor could be used in an anti theft system, etc

Thanks
.
