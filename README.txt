Hello,

Greetings to you..!!

Objective of this app is to, alert the user(on twitter) whenever his home's door is opened.
This small application is developed in python & tested on linux machine(ubuntu) but should work well in Raspberry Pi as well.


Target User:
=============
It was written to be used by anyone interested in IoT (Internet of Things). 
I have developed this small application, keeping in mind that playing with various motion detection sensors, etc might get tricky
for most of the people. 
Therefore this small python app:
i)   tracks the movement of a wireless mouse
ii)  detect opening of a door, with which the mouse is attached
iii) sends alert messages on Twitter


Objective:
===========
To alert the user via twitter, whenever his home's main door opens.


Pre-requisites: 
================
(I) HARDWARE:
	- Linux OS / Raspberry Pi - having sudo access on terminal/console.
	- Wireless Mouse
	- Mobile Phone having Twitter App (Optional)

(II) SOFTWARE:
	- Python
	- Twitter Python package - https://pypi.python.org/pypi/twitter
	- Twitter Account
	- Twitter Application installed in mobile (Optional)


Procedure:
==========

1) Python should be installed. (if not already installed:  sudo apt-get install python )

2) Install twitter package from 
	(a) Visit->  https://pypi.python.org/pypi/twitter
	(b) Click on "Downloads" 
	(c) Save it in your prefered location
	(d) Extract the package
	(e) In the terminal: visit the location & execute->   sudo python setup.py build install 
3) Visit apps.twitter.com & Click on "Create new app" to get the authentication codes.

3) Open "SecureHome.py" file in any text editor and edit the following variables:
	 12 API_KEY = 'XXXX'
	 13 API_SECRET = 'XXXX'
	 14 ACCESS_TOKEN = 'XXXX'
	 15 ACCESS_TOKEN_SECRET = 'XXXX'

4) Optionally in "SecureHome.py" file you can set "debug = 1" for enabling the console logs(enabled by default). Else set "debug = 0" for no logging on console.
	 10 debug = 1

5) Attach(stick/tie) the wireless mouse to the extreme end of the door such that mouse is in contact with the floor, when the door is opened/closed. Make sure that you are able to open & close the door after this modification.

6) Plug-in the bluetooth receiver of the mouse to your server (Linux/Raspberry machine).

7) Start the program on terminal-->  sudo python SecureHome.py

8) Observe the welcome msg. Eg:
"Welcome to SecureHome..!! Initializing System @ Mon Sep  7 03:49:07 2015" 

9) Open the door to see cumilative X & Y co-ordinates on the console. If you have twitter application installed on your mobile, you can get the updates in "messages" section of your twitter account.

10) Observe the Alert messages on console & twitter message. 
Eg." Alert(1) : Someone opened your door at Mon Sep  7 03:49:20 2015 "


For any query / suggestions:
=============================
Please feel free to contact.
Developer: 	Amitesh Anand
Email: 		amitesh.unique@gmail.com
Mobile: 	+91-9711163571


Thank you for using this product..!!
	
