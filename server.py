import socket
import sys
from test import *
from time import sleep 

SERVER_TEAM = "O"


def isCorrectFormat(data):
	
	#print len(data) == 11
	#print data[3] == "|"
	#print data[7] == "|"
	#len(data) == 11 and 
	if data[3] == "|" and data[7] == "|":
		return True
	else:
		return False

#"string of this : boardformat = 000|000|000\n"

HOST = '127.0.0.1'      # Symbolic name meaning the local host
PORT = 50007            # Arbitrary non-privileged port
INVALID_FORMAT = 'This is an invalid format' # we won't response in the future if the format is wrong

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # bind those to the socket 
s.listen(1) #listen on the socket 

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = s.accept()
    transmittedData = ""
    try:
        print >>sys.stderr, 'connection from', client_address

        # we may need some reliability measures here 
        # what if the socket is cut off, what if the full data doesn't reach the socket ?
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(64) # is this a size thing, independent from the data speed?             
            #transmittedData = transmittedData + data
            
            if data:              
               if '\n' in data:
               	transmittedData = transmittedData + data
               	print "move from client",transmittedData
               	if isCorrectFormat(transmittedData):
               		try:
               			response = makeMove(transmittedData,determineMove,SERVER_TEAM)               		
               		except:
               			print "Sending TIE to client"
               			connection.sendall("tie\n")
               			break           
    		            
               		print "Here is my move",response
               		sleep(1)
               		connection.sendall(response)
               		transmittedData = ""
               	else:
               		connection.sendall(INVALID_FORMAT)   
              	 	break
               
               else:              
            	transmittedData = transmittedData + data            
            	
    finally:
        # Clean up the connection
        connection.close()
        print "closing the connection"


s.close()


