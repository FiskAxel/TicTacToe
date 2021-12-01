import MinMaxTree as tree
import StateFunctions as s
import os
import time

state = []
def main():
	tree.buildTree(tree.root)
	while(True):
		game()
		if playAgain() == "noob":
			print("\nGoodbye noob!")
			input()
			break

def game():
	global state
	state = [row[:] for row in s.initialState]
	updateScreen()
	while(True):
		xMove()
		updateScreen()
		if s.winner(state):
			break
		oMove()
		updateScreen()
		if s.winner(state):
			break
	printWinnerMessage()

def xMove():
	"Users turn"
	while True:
		move = intTryParse(input("Make your move: ")) 
		if move and 0 < move and move < 10:
			move = numPadFriendly(move)
			move -= 1
			y, x = int(move / 3), move % 3
			if state[y][x] == '-':
				state[y][x] = 'X'
				return
		print("Invalid Input!")
def oMove():
	"Computers turn"
	print("Omputr's turn...")
	time.sleep(1)
	draw = None
	currentNode = tree.getNode(state)
	for c in currentNode.children:
		if c.winner == 'O':
			s.copyState(state, c.state)
			return
		if c.winner == 'DRAW':
			draw = c
	if draw:
		s.copyState(state, draw.state)
		return
	s.copyState(state, currentNode.children[0].state)
def numPadFriendly(move):
	"To take user-input from numPad in a way that the playing field matches its layout"
	if move == 1:
		return 7
	if move == 2:
		return 8
	if move == 3:
		return 9
	if move == 7:
		return 1
	if move == 8:
		return 2
	if move == 9:
		return 3
	return move
def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return False

def updateScreen():
	os.system('cls')
	print("╔═══════════════╗")
	print("║   TicTacToe   ║")
	print("║  X vs Omputr  ║")
	print("╚═══════════════╝")
	s.printState(state)
def printWinnerMessage():
	time.sleep(1)
	w = s.winner(state)
	if w == "DRAW":
		print(w)
	elif w == 'O':
		print("Omputr is the winner!")
	else:
		print("What?:O ", end="")
		time.sleep(1)
		print("How did you win!?")
	time.sleep(1)
def playAgain():
	print("Type \"noob\" to give up... ")
	time.sleep(1)
	print("Or just press [ENTER] to play again!")
	return input()

main()