"""Missionaries and Cannibals problem"""

from search import * # This file imports utils.py so it should be in the same folder
import sys # System-specific parameters and functions

class MissionariesAndCannibals(Problem) :
	"""Subclass of search.Problem"""
	
	def __init__(self) :
		"""Sets initial state and goal.
		States are representated as a tuple (m, c, b) where
		m is the number of missionaries in left(starting) bank, 
		c is the number of cannibals in left(ending) bank and
		b is the position of the boat (left or right bank)"""
		print ((3, 3, 'left'), (0 , 0 , 'right'))
		super(MissionariesAndCannibals, self).__init__((3, 3, 'left'), (0 , 0 , 'right'))
#_______________________________________________________________
	
	def __isValidState(self, m, c) :
		"""Checks if a state is valid. """
		if m < 0 or c < 0 : # Error ! 
			return False
		if m > 3 or c > 3 : # Error !
			return False	
		if m > c and m != 3 : # There are both cannibals and missionaries in right bank but cannibals are more
			return False
		if m < c and m != 0 : # There are both cannibals and missionaries in left bank but cannibals are more
			return False
		return True
#_______________________________________________________________

	def actions(self, state) :
		print "state before action"
		print state
		"""Returns the actions that can be executed in the state"""
		# possibleActions are all actions that may be executed, but some of 
		# them may lead in invalid state. So possibleActions should be filtered
		possibleActions = [(1, 1), (1, 0), (2, 0), (0,1), (0,2)]
		validActions = [] # It will store only actions that lead in a valid state
		if state[2] == 'left' :
			for possibleAction in possibleActions :
				m = state[0] - possibleAction[0]
				c = state[1] - possibleAction[1]
				if self.__isValidState(m, c) :
					validActions.append(possibleAction)
		else : # right
			for possibleAction in possibleActions :
				m = state[0] + possibleAction[0]
				c = state[1] + possibleAction[1]
				if self.__isValidState(m, c) :
					validActions.append(possibleAction)
#		print len(validActions)
#		for validAction in validActions :
#			print "\t", validAction, self.result(state, validAction)
#			raw_input("pause")
	        print "actions"
		print validActions
		return validActions
#_______________________________________________________________

	def result(self, state, action) :
		""""""
		m = state[0]
		c = state[1]
		b = state[2]
		if b == 'left' :
			m = state[0] - action[0]
			c = state[1] - action[1]
			b = 'right'
		else : # right
			m = state[0] + action[0]
			c = state[1] + action[1]
			b = 'left'
		print "result"
		print (m, c, b)
		return (m, c, b)






p = MissionariesAndCannibals()

s = breadth_first_search(p)
sol = s.solution() # The sequence of actions to go from the root to this node
path = s.path() # The nodes that form the path from the root to this node
print "Solution: \n+{0}+\n|Action\t|State\t	\t|Path Cost |\n+{0}+".format('-'*42)
for i in range(len(path)) :
	state = path[i].state
	cost = path[i].path_cost
	action = " "
	if i > 0 : # The initial state has not an action that results to it
		action = sol[i-1]
	print "|{0}\t|{1} \t|{2} \t   |".format(action, state, cost)
print "+{0}+".format('-'*42)














