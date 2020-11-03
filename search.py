# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #from game import Directions
    #s = Directions.SOUTH
    #w = Directions.WEST
    #print "Start:", problem.getStartState() (5,5)
    #return [s, s, w, s, w, w, s, w]

    start = problem.getStartState() #start =(5,5)# in searchAgent.py
    stack = [] # DFS use stack as its structure
    explored =[]

    stack.append((start,[])) #add start node in the stack, [] is the answer

    while(True): # do a lopp
        now,ans = stack.pop()# take out the top node from the stack, and the variable now is current node and ans is path
        if problem.isGoalState(now):#test the current node if goal or not
            return ans

        if now not in explored:
            for node, direction, cost in problem.getSuccessors(now):#get the successors of node now
                history = ans + [direction]# add history path
                stack.append((node,history))#combine history path to node, if doesnt do that, when the algorithm
                                            #in the deadend and back to the previous node will cause the redundant direction
        if now not in explored:#add node to explored[]
            explored.append(now)
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    stack = util.Queue()#BFS use queue as its struture,
    explored = []

    stack.push((start, []))#add start node in the stack, [] is the answer

    while(True):# do a lopp when stack !=0
        now, ans = stack.pop()# take out the top node from the stack, and the variable now is current node and ans is path
        #print ('now',now)
        if problem.isGoalState(now):  # test the current node is goal or not
            return ans

        if now not in explored:
            for item in problem.getSuccessors(now):

                history = ans + [item[1]]# add history path
                stack.push((item[0], history))#combine history path to node, if doesnt do that, when the algorithm
                                            #in the deadend and back to the previous node will cause the redundant direction

        if now not in explored:#add node to explored[]
            explored.append(now)




def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()  # start =(5,5)
    stack = util.PriorityQueue()#UCS use priorityqueue as a structure
    explored = []

    stack.push((start, [],0),0)#add start node in the stack, [] is the answer

    while(True):# do a lopp when stack !=0
        now, ans,total = stack.pop()# total is the totalcost of the node now
        if problem.isGoalState(now):#test the current node if goal or not
            return ans
        if now not in explored:
            for node, direction, cost in problem.getSuccessors(now):

                totalcost = total + cost
                history = ans + [direction]# add history path
                stack.push((node, history,totalcost), totalcost)#push the totalcost, so the priorityqueue can pop the smallest cost node
        if now not in explored:#add node to explored[]
            explored.append(now)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()  # start =(5,5)
    stack = util.PriorityQueue()
    explored = []

    stack.push((start, [], 0), 0)#add start node in the stack, [] is the answer, the first 0 is history cost, the second
                                #one is expected cost

    while(True):# do a lopp
        now, ans, total = stack.pop()
        if problem.isGoalState(now):#test the current node if goal or not
            return ans
        if now not in explored:
            for node, direction, cost in problem.getSuccessors(now):
            # set a if function to exclude the node have been explored
                totalcost = total + cost#
                history = ans + [direction]# add history path
                expect = totalcost+heuristic(node,problem)# f(n) = g(n)+h(n):totalcost is g(n), heuristic() is h(n)
                stack.push((node, history, totalcost), expect)#add expected cost to the priorityQueue, and let prorityQueue according ot the expected cost to do pop()
        if now not in explored:#add node to explored[]
            explored.append(now)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
