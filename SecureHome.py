# A python program for detecting mouse movement & posting on Twitter:
import struct
import sys
import time

# If not already installed, then download & install twitter package from: 
# https://pypi.python.org/pypi/twitter
from twitter import *

debug = 1

API_KEY = 'XXXX'
API_SECRET = 'XXXX'
ACCESS_TOKEN = 'XXXX'
ACCESS_TOKEN_SECRET = 'XXXX'
twitter_username = 'XXXX'

localtime = time.asctime( time.localtime(time.time()) )
auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter( auth=auth)
welcome_msg = "\nWelcome to SecureHome..!! Initializing System @ " +localtime
print ( welcome_msg )
twitter.direct_messages.new(user=twitter_username,text=welcome_msg  )

file = open( "/dev/input/mice", "rb" )

def getMouseEvent():
	file = open( "/dev/input/mice", "rb" )
	buf = file.read(3)
	button = ord( buf[0] )
	bLeft = button & 0x1
	bMiddle = ( button & 0x4 ) > 0
	bRight = ( button & 0x2 ) > 0
	x,y = struct.unpack( "bb", buf[1:] )
	file.close();
	return x,y


alert_count = 1
posx = 0
posy = 0
while( 1 ):
	x,y = getMouseEvent()
	posx =  posx + x
	posy =  posy + y

	# This should update, when the mouse moves even slightly
	if ( debug == 1 ) :
		print posx , posy 

	# Door is opened and is not just a vibration movement
	if ( posx>100 or posy>100 or  posx < -100 or posy < -100 ) :
		localtime = time.asctime( time.localtime(time.time()) )

		msg = 'Alert(' + str( alert_count ) + ') : Someone opened your door at ' + localtime 

		# Shows the alert msg on console
		if ( debug == 1) :
			print msg

		# Send alert msg via twitter account
		twitter.direct_messages.new(user="anand_amitesh",text=msg )
		
		# Reset / Update the counters for next movement.
		posx = 0
		posy = 0
		alert_count = alert_count + 1

		# Wait for 10 seconds, to avoid too many alert msgs for a single move
		if ( debug == 1) :
			print ("Going to sleep for 10 seconds")

		time.sleep(10) 
	
		# Ready for monitoring next movement
		if ( debug == 1 ) :
			print ( "Ready for monitoring next movement..!!" )


print ( "End of program")
