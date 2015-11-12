"""N-Queens problem"""

from search import *
import sys

class NQueensProblem(Problem) :
        
	"""Subclass of search.Problem"""
	
	def __init__(self, n) :
		"""input n: size of table """
		#print "initialize"
		#print tuple([tuple([0 for i in range(n)]) for j in range(n)])
		super(NQueensProblem, self).__init__(tuple([tuple([0 for i in range(n)]) for j in range(n)]), None)
		
		self.n = n
		
	def actions(self, state) :
                #print state
                
		#print "actions"
		
		#print  [(i+1) for i in range(self.n*self.n) ]
		return [ (i+1) for i in range(self.n*self.n) ]
		
	def result(self, state, action)	:	
	#	print state
		n=self.n		
		#print "result"
	#	print "for action"
	#	print action  
		
		if (action % n==0):
			row=(action/n)-1
			column=n-1
		else:
			row=(action/n)
			column=action%n-1
		#print "row is " 
		#print row
		#print "column is "
		#print column
		#kanw to stuple lista
		newStateList = list(state)
		k=0
		
		for t in newStateList:
			newStateList[k]=list(t)
			k=k+1
		for i in range(0,n):
			if (newStateList[i][row]==3):
				newStateList[i][row]=0 
			else:
				newStateList[i][row]=newStateList[i][row]+1
			if (newStateList[column][i]==3):
				newStateList[column][i]=0 
			else:
				newStateList[column][i]=newStateList[column][i]+1
			#print  newStateList
                if (newStateList[column][row]==0):
			newStateList[column][row]=3
                else:
			newStateList[column][row]=newStateList[column][row]-1
		
	#	print newStateList

		#kanw tin lista stuple
		k=0
		for lista in newStateList:
			newStateList[k]=tuple(lista)
			k=k+1
		#print tuple(newStateList)
		#print newStateList
		
	
		
		#newStateList[2] = 3
		#print tuple(newStateList)
		#print tuple(newStateList)
		return tuple(newStateList)
		#state[2]=3
		#print state[2]
		#print action
		#print state
		# Copy state
		#newStateList = list(state)
			
		#newStateList[i] = j
		#return 1
		
	def goal_test(self, state) :
		lista_stoxou1=list([list([1 for i in range(self.n)]) for j in range(self.n)])
		lista_stoxou2=list([list([2 for i in range(self.n)]) for j in range(self.n)])
		lista_stoxou3=list([list([3 for i in range(self.n)]) for j in range(self.n)])

		newStateList = list(state)
		k=0
		
		for t in newStateList:
			newStateList[k]=list(t)
			k=k+1
		#if (newStateList==[[3,3,3],[3,3,3],[3,3,3]]):
		if (newStateList==lista_stoxou1 or newStateList==lista_stoxou2 or newStateList==lista_stoxou3 ):
			print "vrethike"
			#exit(0)
		        return True
		else:
			return False	
		
	# Useless functions
#	def path_cost(self, c, state1, action, state2) :
#		return c+1
#		
#    def value(self, state) :
#    	return 1
    	
    	
def h1(n) :
	
	return 1	
	#lista_stoxou=[[3 for i in range(n.n)]for j in range(n.n)]
# /////////////////////////////////	






#	state=n.state
#	newStateList = list(state)
#	k=0
		
#	for t in newStateList:
#		newStateList[k]=list(t)
#		k=k+1









	#stoxos=newStateList[k-1][k-1]
	#stoxos2=newStateList[0][0]
	#flag=0
	#flag=0
	#flaga=0
	#for s in range(k):
	#	  if (newStateList[k-1][s]==stoxos):
	#		 flag=flag+1
        
        
	#if  ( flag==k) :
	#	return 1
        
	
#	lista_stoxou1=[[1 for i in range(k)]for j in range(k)]
#	lista_stoxou2=[[2 for i in range(k)]for j in range(k)]
#	lista_stoxou3=[[3 for i in range(k)]for j in range(k)]
	
#	if (lista_stoxou1==newStateList or lista_stoxou2==newStateList or lista_stoxou3==newStateList):
#		return 0
#	else:
#		return 1
#///////////////////////////////////			
	#print "to state einai"
	#return 1;
	#print n.state
	#return 1
	#state = n.state
	#if 0 in state :
	#	i = state.index(0)
	#else :
	#	i = len(state)-1
	#if (i == 0 ) :
	#	return state[0]
	#else :
		#return abs(state[i]-state[i-1])

def h2(n) :
	state = n.state
	if 0 in state :
		i = state.index(0)
	else :
		i = len(state)-1
	if (i == 0 ) :
		return state[0]
	else :
		sum = 0
		for j in range(1, i) :
			sum += abs(state[i]-state[i-1]) 
		return sum*1.0 / i
		
				
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

