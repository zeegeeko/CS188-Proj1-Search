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
    from game import Directions
    closed = []
    fringe = util.Stack()
    fringe.push((problem.getStartState(), [], 0))
    #paths = []

    while not fringe.isEmpty():
        node = fringe.pop()
        paths = node[1]
        if problem.isGoalState(node[0]):
            return paths
        if not node[0] in closed:
            closed.append(node[0]);
            for child in problem.getSuccessors(node[0]):
                fringe.push((child[0], paths + [child[1]] , problem.getCostOfActions(paths + [child[1]])))

    #No Solutions
    return None
#    print "GOAL NOT FOUND!!!"
#    util.raiseNotDefined()

# def pathFinder(edgeDict, start, goal):
#     # returns a path example: [s, w, w, s]
#     from game import Directions
#     path = []
#     stack = util.Stack()
#     node = goal
#     while not node is start:
#         stack.push(node)
#         node = edgeDict[node]
# #    print "PATH="
# #    stack.push(start)
#     parentNode = start
#     while not stack.isEmpty():
#         node = stack.pop()
# #        print parentNode
#         print parentNode[1]
#         if parentNode[1] - node[1] == -1:
#             path.append(Directions.NORTH)
#         if parentNode[1] - node[1] == 1:
#             path.append(Directions.SOUTH)
#         if parentNode[0] - node[0] == -1:
#             path.append(Directions.EAST)
#         if parentNode[0] - node[0] == 1:
#             path.append(Directions.WEST)
#
#         parentNode = node
# #    print path
#     return path

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    closed = []
    fringe = util.Queue()
    fringe.push((problem.getStartState(), [], 0))

    while not fringe.isEmpty():
        node = fringe.pop()
        paths = node[1]
        if problem.isGoalState(node[0]):
            #print paths
            return paths
        if not node[0] in closed:
            closed.append(node[0]);
            for child in problem.getSuccessors(node[0]):
                fringe.push((child[0], paths + [child[1]] , problem.getCostOfActions(paths + [child[1]])))
    #No Solutions
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    closed = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0),0)
    paths = []

    while not fringe.isEmpty():
        node = fringe.pop()
        paths = node[1]
        if problem.isGoalState(node[0]):
            return paths
        if not node[0] in closed:
            closed.append(node[0]);
            for child in problem.getSuccessors(node[0]):
                g_x = problem.getCostOfActions(paths + [child[1]])
                fringe.push((child[0], paths + [child[1]] , g_x), g_x)

    #No Solutions
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    closed = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0),0)
    paths = []

    while not fringe.isEmpty():
        node = fringe.pop()
        paths = node[1]
        if problem.isGoalState(node[0]):
            return paths
        if not node[0] in closed:
            closed.append(node[0]);
            for child in problem.getSuccessors(node[0]):
                g_x = problem.getCostOfActions(paths + [child[1]])
                h_x = heuristic(child[0],problem)
                fringe.push((child[0], paths + [child[1]] , g_x + h_x), g_x + h_x)

    #No Solutions
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
