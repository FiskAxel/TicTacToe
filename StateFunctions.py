initialState = [['-', '-', '-'],
				['-', '-', '-'],
				['-', '-', '-']]

def printState(state):
	print(    "     ┌─────┐")
	for y in state:
		print("     │ ", end="")
		for x in y:
			print(    x, end="")
		print(" │")	
	print(    "     └─────┘")

def player(state):
	"Returns whose turn it is."
	xCount = 0
	oCount = 0
	for y in range(3):
		for x in range(3):
			if state[y][x] == 'X':
				xCount += 1
			if state[y][x] == 'O':
				oCount += 1
	if xCount > oCount:
		return 'O'
	return 'X'
def moves(state):
	"Returns array of all possible moves."
	m = []
	for y in range(3):
		for x in range(3):
			if state[y][x] == '-':
				m.append([y, x])
	return m
def stateAfterMove(state, move, player):
	"Returns what the state will be if inputted move is made."
	y = move[0]
	x = move[1]
	newState = [row[:] for row in state]
	newState[y][x] = player
	return newState
def winner(state):
	"""
	If the game is over the end result will be returned:
	'X', 'O' or 'DRAW'.
	"""
	# Horizontal
	if state[0][0] == state[0][1] and state[0][0] == state[0][2] and state[0][0] != '-':
		return state[0][0]
	if state[1][0] == state[1][1] and state[1][0] == state[1][2] and state[1][0] != '-':
		return state[1][0]
	if state[2][0] == state[2][1] and state[2][0] == state[2][2] and state[2][0] != '-':
		return state[2][0]
	# Vertical
	if state[0][0] == state[1][0] and state[0][0] == state[2][0] and state[0][0] != '-':
		return state[0][0]
	if state[0][1] == state[1][1] and state[0][1] == state[2][1] and state[0][1] != '-':
		return state[0][1]
	if state[0][2] == state[1][2] and state[0][2] == state[2][2] and state[0][2] != '-':
		return state[0][2]
	# Diagonals
	if state[0][0] == state[1][1] and state[0][0] == state[2][2] and state[0][0] != '-':
		return state[0][0]
	if state[0][2] == state[1][1] and state[0][2] == state[2][0] and state[0][2] != '-':
		return state[0][2]
	# No empty tiles
	m = moves(state)
	if len(m) == 0:
		return 'DRAW'

def turn(state):
	"Turns state clockwise."
	t = [row[:] for row in state]
	state[0][0] = t[2][0]
	state[0][1] = t[1][0]
	state[0][2] = t[0][0]
	state[1][0] = t[2][1]
	state[1][2] = t[0][1]
	state[2][0] = t[2][2]
	state[2][1] = t[1][2]
	state[2][2] = t[0][2]
def flip(state):
	"Flips state vertically."
	t = [row[:] for row in state]
	state[0][0] = t[2][0]
	state[0][1] = t[2][1]
	state[0][2] = t[2][2]
	state[2][0] = t[0][0]
	state[2][1] = t[0][1]
	state[2][2] = t[0][2]

def copyState(s1, s2):
	"""Copies s2 to s1.
	Also makes it turned and flipped according to s1's input state.
	s2 should be one move away from s1.
	"""
	t = [row[:] for row in s2]
	align(s1, t)
	for y in range(3):
		for x in range(3):
			s1[y][x] = t[y][x]
def align(s1, s2):
	"Turns and flippes until s2 matches s1."
	for _ in range(2):
		for _ in range(4):
			if aligned(s1, s2):
				return
			turn(s2)
		flip(s2)
def aligned(s1, s2):
	"Checks if there is just one tile difference between s1 and s2."
	diff = 0
	for y in range(3):
		for x in range(3):
			if s1[y][x] != s2[y][x]:
				diff += 1
	if diff > 1:
		return False
	return True