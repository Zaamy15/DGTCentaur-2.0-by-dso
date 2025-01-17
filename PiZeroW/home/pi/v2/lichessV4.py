import sys
import berserk
import ssl
import time
import threading
import boardfunctions
import chess
import v2conf

# Run a game on lichess
# This is version two so we do it directly and with screen control!

# Castling - move king, wait for beep, move rook
# pawn promotion not yet implemented. Pick up pawn, put down queen

# python3 lichess.py [current|New]

# This is our lichess access token, the game id we're playing, fill it
# in in v2conf.py
#
# Note the API requires that the raspberry pi clock has a reasonably
# accurate time for the SSL
token = v2conf.lichesstoken
pid = -1
boardfunctions.clearSerial()

if (len(sys.argv) == 1):
#	print("python3 lichess.py [current|New1]")
	sys.exit()

if (len(sys.argv) > 1):
	if (str(sys.argv[1]) != "current" and str(sys.argv[1]) != "New"):
		#print("python3 lichess.py [current|New2]")
		sys.exit()

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

remotemoves = ""
#changed dso
status = ""
board = chess.Board()

# First start up the screen
boardfunctions.initScreen()
if (sys.argv[1] == "current"):
	boardfunctions.writeText(0, 'Joining Game')
else:
	boardfunctions.writeText(0, 'New Game')
boardfunctions.writeText(1, 'on Lichess')
#boardfunctions.writeText(2, 'LEDs Off')
boardfunctions.ledsOff()

# Get the current player's username
who = client.account.get()
player = str(who.get('username'))
boardfunctions.writeText(2, 'Player:')
boardfunctions.writeText(3, player)

# We'll use this thread to start a game. Probably not the best way to do it but
# let's make the thread pause 5 seconds when it starts up so that we can be
# sure that client.board.stream_incoming_events() has started well

running = True

def newGameThread():
	time.sleep(5)


#mod by dso 3.10.21
	gtime = str(sys.argv[2])
#	print(gtime)
	ginc = str(sys.argv[3])
#	print(ginc)
	grated = str(sys.argv[4])
#	print(grated)
	gcolor = str(sys.argv[5])
#	print(gcolor)
	boardfunctions.writeText(2, f'time {gtime} , {ginc}')
	boardfunctions.writeText(3, f'ratedt={grated}')
	boardfunctions.writeText(4, f'color={gcolor}')
	if (gtime=='10' and ginc=='5' and grated=="False" and gcolor=="white"):
		client.board.seek(10, 5, rated=False, variant='standard', color='white', rating_range=None)
	if (gtime=='10' and ginc=='5' and grated=="False" and gcolor=="black"):
		client.board.seek(10, 5, rated=False, variant='standard', color='black', rating_range=None)
	if (gtime=='10' and ginc=='5' and grated=="False" and gcolor=="random"):
		client.board.seek(10, 5, rated=False, variant='standard', color='random', rating_range=None)
	if (gtime=='10' and ginc=='5' and grated=="True" and gcolor=="white"):
		client.board.seek(10, 5, rated=True, variant='standard', color='white', rating_range=None)
	if (gtime=='10' and ginc=='5' and grated=="True" and gcolor=="black"):
		client.board.seek(10, 5, rated=True, variant='standard', color='black', rating_range=None)
	if (gtime=='10' and ginc=='5' and grated=="True" and gcolor=="random"):
		client.board.seek(10, 5, rated=True, variant='standard', color='random', rating_range=None)
	
	if (gtime=='15' and ginc=='10' and grated=="False" and gcolor=="white"):
		client.board.seek(15, 10, rated=False, variant='standard', color='white', rating_range=None)
	if (gtime=='15' and ginc=='10' and grated=="False" and gcolor=="black"):
		client.board.seek(15, 10, rated=False, variant='standard', color='black', rating_range=None)
	if (gtime=='15' and ginc=='10' and grated=="False" and gcolor=="random"):
		client.board.seek(15, 10, rated=False, variant='standard', color='random', rating_range=None)
	if (gtime=='15' and ginc=='10' and grated=="True" and gcolor=="white"):
			client.board.seek(15, 10, rated=True, variant='standard', color='white', rating_range=None)
	if (gtime=='15' and ginc=='10' and grated=="True" and gcolor=="white"):
		client.board.seek(15, 10, rated=True, variant='standard', color='black', rating_range=None)
	if (gtime=='15' and ginc=='10' and grated=="True" and gcolor=="random"):
		client.board.seek(15, 10, rated=True, variant='standard', color='random', rating_range=None)
	if (gtime=='30' and ginc=='0' and grated=="False" and gcolor=="white"):
		client.board.seek(30, 0, rated=False, variant='standard', color='white', rating_range=None)
	if (gtime=='30' and ginc=='0' and grated=="False" and gcolor=="black"):
		client.board.seek(30, 0, rated=False, variant='standard', color='black', rating_range=None)
	if (gtime=='30' and ginc=='0' and grated=="False" and gcolor=="random"):
		client.board.seek(30, 0, rated=False, variant='standard', color='random', rating_range=None)
	if (gtime=='30' and ginc=='0' and grated=="True" and gcolor=="white"):
		client.board.seek(30, 0, rated=True, variant='standard', color='white', rating_range=None)
	if (gtime=='30' and ginc=='0' and grated=="True" and gcolor=="black"):
		client.board.seek(30, 0, rated=True, variant='standard', color='black', rating_range=None)
	if (gtime=='30' and ginc=='0' and grated=="True" and gcolor=="random"):
		client.board.seek(30, 0, rated=True, variant='standard', color='random', rating_range=None)
	
	if (gtime=='30' and ginc=='20' and grated=="False" and gcolor=="white"):
		client.board.seek(30, 20, rated=False, variant='standard', color='white', rating_range=None)
	if (gtime=='30' and ginc=='20' and grated=="False" and gcolor=="black"):
		client.board.seek(30, 20, rated=False, variant='standard', color='black', rating_range=None)
	if (gtime=='30' and ginc=='20' and grated=="False" and gcolor=="random"):
		client.board.seek(30, 20, rated=False, variant='standard', color='random', rating_range=None)
	if (gtime=='30' and ginc=='20' and grated=="True" and gcolor=="white"):
		client.board.seek(30, 20, rated=True, variant='standard', color='white', rating_range=None)
	if (gtime=='30' and ginc=='20' and grated=="True" and gcolor=="black"):
		client.board.seek(30, 20, rated=True, variant='standard', color='black', rating_range=None)
	if (gtime=='30' and ginc=='20' and grated=="True" and gcolor=="random"):
		client.board.seek(30, 20, rated=True, variant='standard', color='random', rating_range=None)
	
	if (gtime=='60' and ginc=='20' and grated=="False" and gcolor=="white"):
		client.board.seek(60, 20, rated=False, variant='standard', color='white', rating_range=None)
	if (gtime=='60' and ginc=='20' and grated=="False" and gcolor=="black"):
		client.board.seek(60, 20, rated=False, variant='standard', color='black', rating_range=None)
	if (gtime=='60' and ginc=='20' and grated=="False" and gcolor=="random"):
		client.board.seek(60, 20, rated=False, variant='standard', color='random', rating_range=None)
	if (gtime=='60' and ginc=='20' and grated=="True" and gcolor=="white"):
		client.board.seek(60, 20, rated=True, variant='standard', color='white', rating_range=None)
	if (gtime=='60' and ginc=='20' and grated=="True" and gcolor=="black"):
		client.board.seek(60, 20, rated=True, variant='standard', color='black', rating_range=None)
	if (gtime=='60' and ginc=='20' and grated=="True" and gcolor=="random"):
		client.board.seek(60, 20, rated=True, variant='standard', color='random', rating_range=None)
	


# boardfunctions.writeText(7, 'Game ID')

# Wait for a game to start and get the game id!
gameid = ""
if (str(sys.argv[1]) == "New"):
	boardfunctions.writeText(2, 'gamesearch')
	#print("Looking for a game")
	gt = threading.Thread(target=newGameThread, args=())
	gt.daemon = True
	gt.start()
while gameid == "":
	for event in client.board.stream_incoming_events():
		if ('type' in event.keys()):
			if (event.get('type') == "gameStart"):
				
				#print("is gameStart")
				if ('game' in event.keys()):
					#print(event)
					gameid = event.get('game').get('id')
					break

#print("Game started: " + gameid)
boardfunctions.writeText(9, gameid)

playeriswhite = -1
whiteplayer = ""
blackplayer = ""

whiteclock = 0
blackclock = 0
whiteincrement = 0
blackincrement = 0

# Lichess doesn't start the clocks until white moves
starttime = -1

# This thread keeps track of the moves made on lichess
def stateThread():
	global remotemoves
	global status
	global playeriswhite
	global player
	global whiteplayer
	global blackplayer
	global whiteclock
	global blackclock
	global whiteincrement
	global blackincrement
	global resign
	global winner
	while running:
		gamestate = client.board.stream_game_state(gameid)
		for state in gamestate:
			print(state)
#mod by dso 4.1021
			if ('state' in state.keys()):
				remotemoves = state.get('state').get('moves')
				status = state.get('state').get('status')
			else:
				if ('moves' in state.keys()):
					remotemoves = state.get('moves')
				if ('status' in state.keys()):
					status = state.get('status')
			remotemoves = str(remotemoves)
			status = str(status)
# dso add event resign and stop the game
			if status == 'resign':
				winner = str(state.get('winner'))
				status = 'Ende'
				running = False
			if (remotemoves == "None"):
				remotemoves = ""
			if ('black' in state.keys()):
				if ('name' in state.get('white')):
					print(str(state.get('white').get('name')) +
						  " vs " + str(state.get('black').get('name')))
					whiteplayer = str(state.get('white').get('name'))
					blackplayer = str(state.get('black').get('name'))
					if (str(state.get('white').get('name')) == player):
						playeriswhite = 1
					else:
						playeriswhite = 0
			if ('state' in state.keys()):
				if ('wtime' in state.get('state').keys()):
					wtime = int(state.get('state').get('wtime'))
					whiteclock = wtime
					winc = int(state.get('state').get('winc'))
					whiteincrement = winc
				if ('btime' in state.get('state').keys()):
					btime = int(state.get('state').get('btime'))
					blackclock = btime
					binc = int(state.get('state').get('binc'))
					blackincrement = binc

			#time.sleep(1)


#print("Starting thread to track the game on Lichess")
st = threading.Thread(target=stateThread, args=())
st.daemon = True
st.start()
#print("Started")

boardfunctions.beep(boardfunctions.SOUND_GENERAL)
boardmoves = ""
lastboardmove = ""
beeped = 0

while playeriswhite == -1:
	time.sleep(0.1)
#boardfunctions.writeText(7, "Playing as")
#if playeriswhite == 1:
#    boardfunctions.writeText(8, 'White')
#if playeriswhite == 0:
#    boardfunctions.writeText(8, 'Black')

# ready for white
ourturn = 1
if playeriswhite == 0:
	ourturn = 0

boardfunctions.clearBoardData()

oldremotemoves = ""
lastmove = ""
correcterror = -1
halfturn = 0
castled = ""

boardfunctions.clearScreenBuffer()
boardfunctions.writeText(0,blackplayer)
boardfunctions.writeText(9,whiteplayer)
fen = board.fen()
sfen = fen[0 : fen.index(" ")]
baseboard = chess.BaseBoard(sfen)
pieces = []
for x in range(0,64):
	pieces.append(str(chess.BaseBoard(sfen).piece_at(x)))
boardfunctions.drawBoard(pieces)

client.board.post_message(gameid, 'I\'m playing with DGT-Centaur V2 by dso, can\'t chat - I\'m not a bot, sry if it struggle, this Version is in a beta status - have fun' , spectator=False)
resign = 1
while status == "started" and ourturn != 0 and resign != 99:

	if ourturn == 1:
		if playeriswhite == 1:
			currentmover = 1
		else:
			currentmover = 0
	if ourturn == 0:
		if playeriswhite == 1:
			currentmover = 1
		else:
			currentmover = 0
	currentmovestart = time.time()

	if ourturn == 1 and status == "started":
		# Wait for the player's move
#		print('Player move')
		movestart = time.time()
		move = boardfunctions.waitMove()
		boardfunctions.beep(boardfunctions.SOUND_GENERAL)
		# Pass the move through
        
		#resign by dso place a new figure on the board
		resign = 1
		if (len(move) == 1):
			if move[0] <=0:
				gifup = True
				# sende ressign to lichess
				client.board.resign(gameid)
				resign=99
				
			
		if (len(move) == 2):
			fromsq = move[0] * -1
			mylastfrom = fromsq
			tosq = move[1]
			#boardfunctions.writeText(12, 'normal move')
		if (len(move) == 3):
			#boardfunctions.writeText(12, 'kick move')
			# This move should consist of two lifted and one place (two positives, 1 negative)
			# it is a piece take. So the negative that is not the inverse of the positive
			# is the piece that has moved and the positive is the tosq
				
#mod by dso 4.10.21
			tosq = -1

			tosq = move[2]

			fromsq = -1
			if move[0] != (tosq * -1): 
				fromsq = move[0] * -1
			if move[1] != (tosq * -1):
				fromsq = move[1] * -1

		mylastfrom = fromsq
		# Convert to letter number square format
		fromln = boardfunctions.convertField(fromsq)
		#print(fromln)
		toln = boardfunctions.convertField(tosq)
		#print(toln)
		#print("Felder OK?")
		# If the piece is a pawn we should take care of promotion here. You could choose it from
		# the board screen. But I'll do that later!
		# Send the move
		lastmove = fromln + toln
		#print(lastmove)
		#print(castled)
		#print(correcterror)
		if lastmove == castled:
                # If we're castling and this is just the rook move then ignore it
			lastmove = ""
			correcterror = tosq
		if correcterror == tosq:
			boardfunctions.ledsOff()
			correcterror = -1
		else:
			try:
				#print("Checking validity")
				mv = chess.Move.from_uci(lastmove)
				#print("Checked")
				if (mv in board.legal_moves):
					board.push(mv)
					if lastmove == "e1g1":
							castled = "h1f1"
					if lastmove == "e1c1":
							castled = "a1d1"
					if lastmove == "e8g8":
							castled = "h8f8"
					if lastmove == "e8c8":
							castled = "a8d8"
					ourturn = 0
					#print("Making move with client")
					ret = client.board.make_move(gameid, fromln + toln)
					#print("Made move with client")
					halfturn = halfturn + 1
				else:
					#print("not a legal move checking for half turn")
					if halfturn != 0:
						#print("Not a legal move!")
						#print(board.legal_moves)
						boardfunctions.clearBoardData()
						boardfunctions.beep(boardfunctions.SOUND_WRONG_MOVE)
						correcterror = fromsq
			except:
				#print("exception checking for half turn")
				if halfturn != 0:
					#print("Not a legal move!")
					#print(board.legal_moves)
					boardfunctions.clearBoardData()
					boardfunctions.beep(boardfunctions.SOUND_WRONG_MOVE)
					correcterror = fromsq
		playertime = time.time()
		#print(board)

		if playeriswhite == 1:
			whiteclock = whiteclock + whiteincrement
			whiteclock = whiteclock - ((playertime - movestart)*1000)
			
		else:
			blackclock = blackclock + blackincrement
			blackclock = blackclock - ((playertime - movestart)*1000)
			

		wtext = ""
		# dso timefix 5.10.21
		if whiteclock//60000 < 1:
			wtext = "0:" + str(whiteclock//1000) + " min      "
		else:
			wtext = str(int(whiteclock//60000))+":"+str(whiteclock//1000) + " mins      "
		boardfunctions.writeText(10,wtext)
		btext = ""
		if blackclock // 60000 < 1:
			btext = "0:" + str(blackclock//1000) + " min      "
		else:
			btext = str(int(blackclock//60000))+":"+ str(blackclock//1000) + " mins      "
		boardfunctions.writeText(1, btext)

	fen = board.fen()
	sfen = fen[0 : fen.index(" ")]
	baseboard = chess.BaseBoard(sfen)
	pieces = []
	for x in range(0,64):
		pieces.append(str(chess.BaseBoard(sfen).piece_at(x)))
	boardfunctions.drawBoard(pieces)
	boardfunctions.writeText(12,str(mv))
	if ourturn == 0 and status == "started":
        # Here we wait to get a move from the other player on lichess
		
		movestart = time.time()
		while status == "started" and str(remotemoves)[-4:] == lastmove:
			time.sleep(0.5)
		if status == "started":
			# There's an incoming move to deal with
		#	print('Player move get in')
			lichesstime = time.time()
			boardfunctions.beep(boardfunctions.SOUND_GENERAL)
			rr = "   " + str(remotemoves)
			lrmove = rr[-5:].strip()
			lrmove = lrmove[:4]
			lrfrom = lrmove[:2]
			lrto = lrmove[2:4]
			lrfromcalc = (ord(lrfrom[:1]) - 97) + ((int(lrfrom[1:2]) - 1) * 8)
			lrtocalc = (ord(lrto[:1]) - 97) + ((int(lrto[1:2]) - 1) * 8)
			boardfunctions.clearBoardData()
			boardfunctions.ledFromTo(lrfromcalc, lrtocalc)
			# Then wait for a piece to be moved TO that position
			movedto = -1
			while movedto != lrtocalc and status == "started":
				move = boardfunctions.waitMove()
				#print('player moves for lichesuser')
				valid = 0
				if move[0] == lrtocalc:
					valid = 1
				if len(move) > 1:
					if move[1] == lrtocalc:
						valid = 1
				if len(move) == 3:
					if move[2] == lrtocalc:
						valid = 1
				if valid == 0:
					boardfunctions.beep(boardfunctions.SOUND_WRONG_MOVE)
				movedto = lrtocalc 
			boardfunctions.beep(boardfunctions.SOUND_GENERAL)
			boardfunctions.clearSerial()
			mv = chess.Move.from_uci(rr[-5:].strip())
			board.push(mv)
			boardfunctions.ledsOff()
			ourturn = 1
			#print('lichess move abgeschlossen')

		#print(board)
# dso timefix 5.10.21
		if playeriswhite == 0:
			whiteclock = whiteclock + whiteincrement
			whiteclock = whiteclock - ((lichesstime - movestart) * 1000)
			
		else:
			blackclock = blackclock + blackincrement
			blackclock = blackclock - ((lichesstime - movestart) * 1000)
			


		wtext = ""
		if whiteclock//60000 < 1:
			wtext = "0:" + str(whiteclock//1000) + " min      "
		else:
			wtext = str(int(whiteclock//60000))+":"+str(whiteclock//1000) + " mins      "
		boardfunctions.writeText(10,wtext)
		btext = ""
		if blackclock // 60000 < 1:
			btext = "0:" + str(blackclock//1000) + " min      "
		else:
			btext = str(int(blackclock // 60000))+":"+ str(blackclock//1000) + " mins      "
		boardfunctions.writeText(1, btext)


		if starttime < 0:
			starttime = time.time()

	fen = board.fen()
	sfen = fen[0 : fen.index(" ")]
	baseboard = chess.BaseBoard(sfen)
	pieces = []
	for x in range(0,64):
		pieces.append(str(chess.BaseBoard(sfen).piece_at(x)))
	boardfunctions.drawBoard(pieces)
	boardfunctions.writeText(12,str(mv))

running = False
if resign == 99 :
	boardfunctions.writeText(11, 'Player resign')
else:
	boardfunctions.writeText(11, 'Game over')
	boardfunctions.writeText(12, f'Winner: {winner}'
time.sleep(2)
boardfunctions.sleepScreen()
# sys.exit()