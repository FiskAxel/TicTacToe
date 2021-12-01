import StateFunctions as s
class node:
	def __init__(self, state, parent):
		self.state = state
		self.parent = parent
		self.children = []
		self.winner = None # The end result from this node if X and O plays flawlessly. 

nodeMap = {} # Takes a state-string as key to get its node-representation from the tree.
root = node(s.initialState, None)
def buildTree(current):
	"""Creats MinMaxTree.
	Nodes represent all its equal states (flipped and rotated) so it's pruned a bit.
	Not alpha-beta pruned since a player can make mistakes.
	"""
	winner = s.winner(current.state)
	if winner:
		current.winner = winner
		current.children = None
		return winner

	for m in s.moves(current.state):
		player = s.player(current.state)
		childState = s.stateAfterMove(current.state, m, player)
		if visited(childState):
			repNode = nodeMap[findKey(childState)]
			winner = repNode.winner
			if repNode not in current.children:
				current.children.append(repNode)
		else:
			child = node(childState, current)
			current.children.append(child)
			nodeMap[makeKey(childState)] = child
			winner = buildTree(child)

		if current.winner == None:
			current.winner = winner
		elif winner == player:
			current.winner = winner
		elif current.winner != player and winner == "DRAW":
			current.winner = winner

	return current.winner
def visited(state):
	"Checks if 'state' is represented in the tree."
	t = [row[:] for row in state]
	for _ in range(2):
		for _ in range(4):
			if makeKey(t) in nodeMap:
				return True
			s.turn(t)	
		s.flip(t)
	return False
def makeKey(state):
	"Returns 'state' in string format."
	output = ""
	for y in range(3):
		for x in range(3):
			output += state[y][x]
	return output

def getNode(state):
	"Returns the node containing the representatin of 'state'."
	return nodeMap[findKey(state)]
def findKey(state):
	"Turns and flips 'state' to find the way it is represented in the tree."
	t = [row[:] for row in state]
	for _ in range(2):
		for _ in range(4):
			key = makeKey(t)
			if key in nodeMap:
				return key
			s.turn(t)
		s.flip(t)