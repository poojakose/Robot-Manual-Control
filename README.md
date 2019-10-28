# Robot-Manual-Control
Requirements :
Raspberry Pi B3+
Dual DC Motor driver 20A
DC Motors (12V 60RPM) - 2
Connecting Wires
SMPS 12v 5A to 10A / Battery 12v 5A to 9A

Step 1. : Hardware connections :-
Signal Pins of Motor Driver Connection with Raspberry PiRead the name given on the motor diver and connect to raspberry pi by checking pins accordingly. BCM is nothing but GPIO pin numbers. Ensure to connect "Ground" properly. 
There are 6 terminal headers on the motor driver just opposite to the signal pins. 2 of them in the middle are for power supply. Connect the positive '+' and negative '-' terminals of battery properly. The rest of the 4 are for connecting motors in a pair of two. Connect the positive '+' and negative '-' terminals of the motor in the end terminals of the motor driver. You can switch the terminals if you get the opposite direction of the motor.
Dual DC Motor driverThen power on the raspberry pi and proceed to install and write scripts .

Step 2. : Get your Raspberry pi ready :-
I assume that raspberry pi is ready installed any preferred OS and other basic stuffs like python. Now setup Flask framework to create web server which provides a way to send or receive commands from webpage to Raspberry pi. Install a flask support package into the Raspberry Pi : 

$ pip install Flask

Create a folder named /templates and copy the html script inside as robot.html 
Web Control : Output of robot.htmlNow create a python script outside the /templates folder with any name and name.py extension. Note : replace the IP address to yours raspberry pi's IP " app.run(host='0.0.0.0',port=5010) " . 0
