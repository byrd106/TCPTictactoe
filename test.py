import random

def win(board,character):
	board = list(board)	
	cleanBoard(board)
	if board[0]==character and board[1]==character and board[2]==character:
		return True
	if board[3]==character and board[4]==character and board[5]==character:
		return True
	if board[6]==character and board[7]==character and board[8]==character:
		return True
	if board[0]==character and board[3]==character and board[6]==character:
		return True	
	if board[1]==character and board[4]==character and board[7]==character:
		return True	
	if board[2]==character and board[5]==character and board[8]==character:
		return True		
	if board[0]==character and board[4]==character and board[8]==character:
		return True
	if board[2]==character and board[4]==character and board[6]==character:
		return True

	return False


def firstMove(board,boardLayout = None):
	return board[0]

def randomMove(board,boardLayout = None):
	return random.choice(board)

def getEmptyBoard():
	return "---|---|---\n"

def determineMove(board):
	#print board
	return randomMove(board)

def connectRow(indexList,board): 
	row = []
	for i in indexList:
		row.append(board[i])
	return row

def rowCheck(i,j,board):
	return (board[i] !="-" and board[j] != "-" and board[i] == board[j])


def basicMove(boardSpaces,board):
	
	# 0 1 2 
	# 3 4 5
	# 6 7 8 

	#row rules 
	#col rules 
	#diagonal rules 

	moveList = [
		[0,1,2],
		[3,4,5],
		[6,7,8],
		
		[0,3,6],
		[1,4,7],
		[2,5,8],
		
		[0,4,8],
		[2,4,6]
		
	]


	for t in moveList:
		if rowCheck(t[0],t[1],board):
			if board[t[2]]=="-":
				return t[2]
		if rowCheck(t[1],t[2],board):
			if board[t[0]]=="-":
				return t[0]
		if rowCheck(t[0],t[2],board):
			if board[t[1]]=="-":
				return t[1]

	return randomMove(boardSpaces)

def smartMove(boardSpaces,board):
	
	boardRows = [] 

	boardRows.append(board[0:3]) 
	boardRows.append(board[2:5]) 
	boardRows.append(board[4:7]) 

	boardRows.append(connectRow([0,3,6],board)) 
	boardRows.append(connectRow([1,4,7],board)) 
	boardRows.append(connectRow([2,5,7],board)) 

	erows = []
	for r in boardRows:
		counts = {}
		for k,char in enumerate(r):
			#print k,char
			if char !="-":
				if char not in counts.keys():
					counts[char] = 1
				else: 
					counts[char] = counts[char] + 1

		for key in counts.keys():
			if counts[key] == 2:
				erows.append(r)
		print "HERE ARE THE COUNTS",counts
		
	print "BEBE",erows


	print boardRows
	erows = []
	singleRows = []
	for r in boardRows:
		rc = 0
		for k in r:
			if board[k] != "-":
				rc = rc + 1

		if rc == 2: 
			erows.append(r)
		if rc == 1:
			singleRows.append(r)

	sortedRows = erows+singleRows
	if len(sortedRows) == 0:
		return randomMove(board)
	else:
		return randomMove(sortedRows[0])

	#return erows+singleRows

	# print board[2:5]
	# print board[4:7]
	# print connectRow([0,3,6])
	# print board[0]
	# print board[3] #4 #5 
	# print board[6]
	# print connectRow([1,4,7])
	# print board[1]
	# print board[4]
	# print board[7]
	## print connectRow([2,5,8])
	# print board[2]
	# print board[5]
	# print board[8]
	#print board[2:7]
	#board[index] for index in [1,3,5]
	#print board[i%2==1]
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

def serverWin():
	return "Owins\n"

def clientWin():
	return "Xwins\n"

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
	
	if win(board,"X"):
		raise ValueError('Xwins\n')

	if win(board,"O"):
		print "O WINS!!!!!!"
		raise ValueError('Owins\n')

	if rspaces == []:
		raise ValueError('tie\n')
	
	moveIndex = moveFunction(rspaces,data)
	del data[moveIndex]
	data.insert(moveIndex, team)	
	buildBoard(data)
	return ''.join(data)


def isCorrectFormat(data):
	if len(data) == 12 and data.find('\n') == 11 and data[3] == "|" and data[7] == "|":
		return True
	else:
		return False
	
# board = makeMove("---|---|---\n",basicMove,"X")
# board = makeMove(board,basicMove,"O")
# board = makeMove(board,basicMove,"X")
# board = makeMove(board,basicMove,"O")
# board = makeMove(board,basicMove,"X")
# board = makeMove(board,basicMove,"O")
# print board

def printb(board):
	print board[0]+board[1]+board[2]
	print board[4]+board[5]+board[6]
	print board[8]+board[9]+board[10]
	#print " ======= "
	#print " ======= "


# board = getEmptyBoard()
# i = 0
# while(True):
# 	if i % 2 == 0:
# 		board = makeMove(board,basicMove,"X")
# 	else:
# 		board = makeMove(board,basicMove,"O") 
# 	printb(board)
# 	i+=1


# board = "O--|---|O--\n"
# printb(board)
# board = makeMove(board,basicMove,"X")
# printb(board)
# board = makeMove(board,basicMove,"O")
# printb(board)
# board = makeMove(board,basicMove,"X")
# printb(board)
# board = makeMove(board,basicMove,"O")
# printb(board)
# board = makeMove(board,basicMove,"X")
# printb(board)
# board = makeMove(board,basicMove,"O")
# printb(board)
# board = makeMove(board,basicMove,"X")
# printb(board)
# board = makeMove(board,basicMove,"O")

#board = makeMove(board,basicMove,"O")
#board = makeMove(board,basicMove,"X")

#board = makeMove(board,basicMove(),"X")
#print board
#makeMove("---|---|---\n")
#makeMove("---|---|---\n")

#"-XO|---|---\n"
#"-XO|---|---\n"

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
