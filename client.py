import socket
import sys
from test import *
from time import sleep

CLIENT_TEAM = "X"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 707)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    board = getEmptyBoard()
    message = makeMove(board,randomMove,CLIENT_TEAM)
    sock.sendall(message)
    
    while True:
	    boardSet = ""
	    print "Starting this loop"
	    while 1:	    	
	    	data = sock.recv(64)
	    	#if #tie comes back , shut it down 
	    	if data:	    			    		
	    		if '\n' in data:	
	    			boardSet = boardSet + data
	    			break
	    		else:
	    			boardSet = boardSet + data
	   
	    print "Here is board from server",boardSet
	    print "--"

	    if tieMessage() in boardSet:
	    	print "GOT tie from server"
	    	break

	    myMove = makeMove(boardSet,determineMove,CLIENT_TEAM)
	    print "Here is my move",myMove

	    if gameIsDone(myMove):
	    	myMove = myMove + tieMessage()

	    sock.sendall(myMove)
	  

finally:
    print 'closing socket'
    sock.close()
