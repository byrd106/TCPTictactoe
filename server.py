import socket
import sys
from test import *
from time import sleep 


SERVER_TEAM = "O"

def isCorrectFormat(data):

	if data[3] == "|" and data[7] == "|":
		return True
	else:
		return False



HOST = "0.0.0.0"      # Symbolic name meaning the local host
PORT = 707            # Arbitrary non-privileged port
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
               	print "CLIENT SAYS"
                if tieMessage() in transmittedData:
                  print "I(SERVER,"+SERVER_TEAM+") SAY",tieMessage()
                  connection.sendall(tieMessage())
                  break
                if serverWin() in transmittedData:       
                  print "I(SERVER,"+SERVER_TEAM+") SAY",serverWin()
                  connection.sendall(serverWin())
                  break

                printb(transmittedData)
               	if isCorrectFormat(transmittedData):
               	  try:
                    response = makeMove(transmittedData,basicMove,SERVER_TEAM)              
               	  except ValueError as VE:
                    print "I(SERVER,"+SERVER_TEAM+") SAY"
                    print str(VE)
                    connection.sendall(str(VE))
                    break            
                                 
                  print "I(SERVER,"+SERVER_TEAM+") SAY"
                  printb(response)
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


