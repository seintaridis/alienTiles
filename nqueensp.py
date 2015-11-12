"""N-Queens problem"""

from search import *
import sys
from math import ceil

class NQueensProblem(Problem) :
	"""Subclass of search.Problem"""
	
	def __init__(self, n) :
		"""input n: size of table """
		super(NQueensProblem, self).__init__(tuple([tuple([0 for x in range(n)]) for y in range(n)]), None)
		print self.initial		
		self.n = n

	def actions(self, state) :		
		print "--ACTIONS--"		
		return  [ [i / self.n , i% self.n] for i in range(self.n * self.n) ]


	def result(self, state, action) :
		print "--RESULT--"		
		i = action[0]
		j = action[1]
		n=len(state)
		print "len state:",n
		# Copy state
		newStateList = list(state)
		for x in range(n):
			newStateList[x]=list(newStateList[x])
		print newStateList
		for x in range(n):
			for y in range(n):
				if x==i or y==j :
					if newStateList[x][y] == 3:
						newStateList[x][y] = 0
					else:
						newStateList[x][y] = newStateList[x][y] + 1
		print newStateList
		for x in range(n):
			newStateList[x]=tuple(newStateList[x])
		return tuple(newStateList)
		
	def goal_test(self, state) :
		print "--GOAL TEST--"		
		count_g = 0		
		count_b = 0
		count_p = 0
		s = self.n * self.n
		print "N=" , s
		print state
		for i in range(self.n):
			for j in range(self.n):
				if state[i][j] == 1:
					count_g += 1
				if state[i][j] == 2:
					count_b += 1
				if state[i][j] == 3:
					count_p += 1
		if count_g == s or count_b == s or count_p == s:
			return True
		return False
		
		
	# Useless functions
#	def path_cost(self, c, state1, action, state2) :
#		return c+1
#		
#    def value(self, state) :
#    	return 1
    	
    	
def h1(n) :
	return 1

def h2(n) :
	state = n.state
	n=len(state)
	count_g = 0		
	count_b = 0	
	count_p = 0
	count_r = 0
	print "Heuretic function on state:", state
	for i in range(n):
		for j in range(n):
			if state[i][j] == 1:
				count_g += 1
			if state[i][j] == 2:
				count_b += 1
			if state[i][j] == 3:
				count_p += 1
			if state[i][j] == 0:
				count_r += 1	
	ret = count_p*4.0 + count_r*3.0 + count_g
	#ret = float(ret)/(2*n-1)
	ret = ceil(ret)	
	print "Heuretic result is: ",ret ,"using counters", count_r, count_g, count_b, count_p
	return ret
				
p = NQueensProblem(int(sys.argv[1]))
#print p.initial, type(p.initial)
#for a in p.actions(p.initial) :
#	print p.result(p.initial, a)
print "N:", sys.argv[1], "- Heuristic:", sys.argv[2]
if sys.argv[2] == "1" :
	solution = astar_search(p, lambda node : h1(node))
else :
	solution = astar_search(p, lambda node : h2(node))
	
l = list(solution.state)
#for r in l :
#	sys.stdout.write("+")
#	sys.stdout.write("-"*(len(l)*2-1))
#	sys.stdout.write("+\n")
#	for c in range(len(l)) :
#		if ( c != r-1 ) :
#			sys.stdout.write('|o') 
#		else :
#			sys.stdout.write('|x');
#	sys.stdout.write('|\n')

