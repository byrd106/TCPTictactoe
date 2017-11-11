import socket
import sys
from test import *
from time import sleep
import sys


CLIENT_TEAM = "X"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (sys.argv[1], 707)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    board = getEmptyBoard()
    message = makeMove(board,randomMove,CLIENT_TEAM)

    print "I(CLIENT,"+CLIENT_TEAM+") SAY",message
    sock.sendall(message)
    
    while True:
	    boardSet = ""
	 
	    while 1:	    	
	    	#print "SOCKET",data
	    	data = sock.recv(64)
	    	#if #tie comes back , shut it down 
	    	if data:	    			    		
	    		if '\n' in data:	
	    			boardSet = boardSet + data
	    			break
	    		else:
	    			boardSet = boardSet + data
	   	

	   	#print "SERVER SAYS",data

	    if tieMessage() in boardSet:
	    	print "I(CLIENT,"+CLIENT_TEAM+") SAY",tieMessage()
	    	sock.sendall(tieMessage())
	    	break
	    if serverWin() in boardSet:	    	
	    	print "I(CLIENT,"+CLIENT_TEAM+") SAY",serverWin()
	    	sock.sendall(serverWin())
	    	break
	    if clientWin() in boardSet: 
	    	print "I(CLIENT,"+CLIENT_TEAM+") SAY",clientWin()
	    	sock.sendall(clientWin())
	    	break

	    try:
	    	print "SERVER SAYS"
	    	printb(boardSet)
	    	myMove = makeMove(boardSet,basicMove,CLIENT_TEAM)  
	    except ValueError as VE:
	    	print "I(CLIENT,"+CLIENT_TEAM+") SAY"	
	    	print str(VE)
	    	sock.sendall(str(VE))
	    	break
	
	    print "I(CLIENT,"+CLIENT_TEAM+") SAY"
	    printb(myMove)
	    sock.sendall(myMove)
	  
finally:
    print 'closing socket'
    #sock.close()
