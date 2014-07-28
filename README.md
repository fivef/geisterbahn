Geisterbahn
===========

user:pi
pw:pi

ip if no dhcp server found: 192.168.0.16

Installation
------------

Installation on Rasppi:
see http://opendmx.net/index.php/OLA_Debian_/_Ubuntu#Raspbian


	1. /etc/apt/sources.list
	2. deb   http://apt.openlighting.org/raspbian  wheezy main
	3. sudo apt-get update
	4. sudo apt-get install ola ola-python ola-conf-plugins -y
	5. sudo ola_conf_plugins.sh disable all
	6. sudo ola_conf_plugins.sh enable ftdidmx
	7. sudo service olad restart

Configuration
-------------
ola webinterface http://192.168.0.16:9090/ola.html

add universe

Python API Doc

Autostart in /etc/init.d/rc.local : python /home/pi/dev/geisterbahn/bewegungsmelder_rauch.py&

Bewegungsmelder:
Modul: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview
Pin GPIO 23 und 5V und Masse
und Pin GPIO 24

Lightbar: 
5 channel mode  Red, Green, Blue, Brightness, Strobo

