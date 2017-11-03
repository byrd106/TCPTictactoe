import random

def randomMove(board):
	return random.choice(board)

def getEmptyBoard():
	return "---|---|---\n"

def determineMove(board):
	return randomMove(board)

def getRemainingSpaces(board):
	#print board
	spaces = [i for i, j in enumerate(board) if j == '-']
	return spaces

def gameIsDone(board):
	if board == "":
		return False
	#print "testing if the game is done",board,getRemainingSpaces(board)
	return len(getRemainingSpaces(board)) == 0 # should be 0 

def tieMessage():
	return "tie\n"

def cleanBoard(data):
	data.remove("|")
	data.remove("|")
	data.remove("\n")

def buildBoard(data):
	data.insert(10,"\n")
	data.insert(6,"|")
	data.insert(3,"|")

def makeMove(board,moveFunction,team):
	data = list(board)
	cleanBoard(data)
	rspaces = getRemainingSpaces(data)
	#print rspaces,board
	if rspaces == []:
		raise ValueError('GAME IS FINISHED')
	moveIndex = moveFunction(rspaces)
	del data[moveIndex]
	data.insert(moveIndex, team)	
	buildBoard(data)
	return ''.join(data)


def isCorrectFormat(data):
	if len(data) == 12 and data.find('\n') == 11 and data[3] == "|" and data[7] == "|":
		return True
	else:
		return False
	



#return len(data) == 19 and data[3] == "|" and data[7] == "|"
#board = "XXX|XXX|XX-\n"
#cleanBoard(board)
#print getRemainingSpaces(board)
# try:
# 	board = makeMove(board,determineMove,"X")
# 	print "MOVED"
# except:
# 	print board,"GAME DONE"

# try:
# 	print makeMove(board,determineMove,"X")
# 	print "MOVED"
# except:
# 	print board,"GAME DONE"

#print isCorrectFormat("000|000|000\n")
#print makeMove("XXX|000|000\n",randomMove)
#print isCorrectFormat("000|000|003")


#100|000|000 
#if i am AI id look for board options, 
#if player is close to winning, block them
#if one is open, use it ... 
