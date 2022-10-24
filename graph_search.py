import random
from SearchNode import SearchNode
import collections
import numpy

def euclid_distance(state, goal):
    x = numpy.abs(state[0] - goal[0])
    y = numpy.abs(state[1] - goal[1])
    return numpy.sqrt((x * x) + (y * y))
#==============================================================================
# GRAPH_SEARCH
#
# The fringe and closed list must be drawn while the thinking takes place.
# - Draw the closed list blue (255, 0, 0).
# - Draw the fringe in green (0, 255, 0).
#
# There must be NO console printing in this python file. Make sure you remove
# them or comment them out when you are done.
#==============================================================================
def graph_search(problem=None,
                 Node=None,
                 fringe=None,
                 closed_list=None,
                 view0=None,
                 ):

    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    solution = []
    """
    This is the incorrect Version, Needs to be fixed.

    Correct solution looks like:
    closed list is empty
    fringe has the initial state
    While fringe not empty:
        pull a state,s, from the fringe.
        check to see if s is a goal state.
        if it is:
            return the search node, for walking back to root.
        else:
            add s.state() to closed list
            expand s to s0 with action a0 ... sn to an
            if s0 not in fringe or closed list:
                add s0 to fringe
                point s0 to s with parent action a0
            repeat for s1 ... sn
    """


#Test Code:
    fringe.put(Node)
    maze = problem.maze
    while len(fringe) > 0:
        s = fringe.get()
        state = s.state
        #print(state)
        if problem.goal_test(state):
            solution.append(s)
            while s.parent != None:
                s = s.parent
                solution.append(s)
                solution = solution[::-1]
                #for node in solution:
                    #print(node.state, ' ', node.parent_action)
            return solution
        closed_list.put(state)
        for nodes in problem.successors(state):
            action = nodes[0]
            r,c = nodes[1]
            if (r,c) in closed_list.xs:
                pass
            else:
                fringe.put(SearchNode((r,c), s, action))
            if view0:
                if len(closed_list) == 1:
                    view0['maze'].background[(r,c)] = (0,255,0)
                else:
                    for state in closed_list.xs:
                        r,c = state
                        if view0['maze'].background[r,c] != [0,0,0]:
                            if (r,c) == problem.get_initial_state():
                                view0['maze'].background[r,c] = [0,255,0]
                            else:
                                view0['maze'].background[r,c] = [255,0,0]
                            for node in fringe:
                                r,c = node.state
                                view0['maze'].background[r,c] = [0,0,255]
                view0.run() # Draw everything
            
        
    return None # None is used to indicate no solution

    
def iddfs_graph_search(problem=None,
                       Node=None,
                       fringe=None,
                       closed_list=None,
                       depth=None,
                       view0=None,
):

    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    solution = []
    """
    This is the incorrect Version, Needs to be fixed.

    Correct solution looks like:
    closed list is empty
    fringe has the initial state
    While fringe not empty:
        pull a state,s, from the fringe.
        check to see if s is a goal state.
        if it is:
            return the search node, for walking back to root.
        else:
            add s.state() to closed list
            expand s to s0 with action a0 ... sn to an
            if s0 not in fringe or closed list:
                add s0 to fringe
                point s0 to s with parent action a0
            repeat for s1 ... sn
    """


#Test Code:
    fringe.put(Node)
    maze = problem.maze
    while len(fringe) > 0:
        s = fringe.get()
        state = s.state
        current_depth = s.depth
        #print(state)
        if problem.goal_test(state):
            solution.append(s)
            while s.parent != None:
                s = s.parent
                solution.append(s)
                solution = solution[::-1]
                #for node in solution:
                    #print(node.state, ' ', node.parent_action)
            return solution
        closed_list.put(state)
        for nodes in problem.successors(state):
            action = nodes[0]
            r,c = nodes[1]
            if (r,c) in closed_list.xs or current_depth + 1 > depth:
                pass
            else:
                fringe.put(SearchNode((r,c), s, action, current_depth + 1))
            if view0:
                if len(closed_list) == 1 :
                    view0['maze'].background[(r,c)] = (0,255,0)
                else:
                    for state in closed_list.xs:
                        r,c = state
                        if view0['maze'].background[r,c]:
                            if (r,c) == problem.get_initial_state():
                                view0['maze'].background[r,c] = [0,255,0]
                            else:
                                view0['maze'].background[r,c] = [255,0,0]
                            
                    for node in fringe:
                        view0['maze'].background[r,c] = [0,0,255]
                view0.run() # Draw everything
            
        
    return None # None is used to indicate no solution

def ucs_graph_search(problem=None,
                     Node=None,
                     fringe=None,
                     closed_list=None,
                     trap = None,
                     view0=None,
                     sType = 'ucs'
                 ):

    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    solution = []
    trapStates = []
    for i in trap:
        trapStates.append(i[0])

    print (trapStates)
    

#Test Code:
    fringe.put(Node)
    maze = problem.maze
    while len(fringe) > 0:
        s = fringe.get()
        state = s.state
        heuristic = 0
        if sType == 'ucs':
            pass
        else:
            heuristic = euclid_distance(state, problem.goal_states[0])
        #print(state)
        if problem.goal_test(state):
            solution.append(s)
            while s.parent != None:
                s = s.parent
                solution.append(s)
                solution = solution[::-1]
                #for node in solution:
                    #print(node.state, ' ', node.parent_action)
            return solution
        closed_list.put(state)
        for nodes in problem.successors(state):
            action = nodes[0]
            r,c = nodes[1]
            if (r,c) in closed_list.xs:
                pass
            else:
                if (r,c) in trapStates:
                    index = trapStates.index((r,c))
                    cost = trap[index][1]
                    fringe.put(SearchNode((r,c), s, action, None, (cost + heuristic)))
                else:
                    fringe.put(SearchNode((r,c), s, action, None, (1+heuristic)))
            if view0:
                if len(closed_list) == 1:
                    view0['maze'].background[(r,c)] = (0,255,0)
                else:
                    for state in closed_list.xs:
                        r,c = state
                        if view0['maze'].background[r,c] != [0,0,0]:
                            if (r,c) == problem.get_initial_state():
                                view0['maze'].background[r,c] = [0,255,0]
                            elif (r,c) in trapStates:
                                view0['maze'].background[r,c] = [255,255,0]
                            else:
                                view0['maze'].background[r,c] = [255,0,0]
                    for node in fringe:
                        r,c = node.state
                                
                        if (r,c) in trapStates:
                            view0['maze'].background[r,c] = [255,255,0]
                        else:
                            view0['maze'].background[r,c] = [0,0,255]
                view0.run() # Draw everything
            
        
    return None # None is used to indicate no solution

def bts_graph_search(problem=None,
                     Node=None,
                     solution = None,
                     view0=None,
):

    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    #print(Node.state)
    solution.append((Node.state))
    
    #Color
    if view0['maze'].background[Node.state] != [0,0,0]:
        if Node.state == problem.get_initial_state():
            view0['maze'].background[Node.state] = [0,255,0]
        else:
            view0['maze'].background[Node.state] = [255,0,0]

     # Draw everything

    #Test Goal State
    if problem.goal_test(Node.state):
        return solution
        
    for nodes in problem.successors(Node.state):
        newNode = SearchNode(nodes[1])
        test = problem.goal_test(newNode.state)
        if test:
            solution.append((newNode.state))
            view0['maze'].background[newNode.state] = [255,0,0]
            view0.run()
            break
        else:
            if newNode.state not in solution:
                bts_graph_search(problem = problem,
                                 Node = newNode,
                                 solution = solution,
                                 view0 = view0)
                if not problem.goal_test(solution[-1]):
                    solution.remove((newNode.state))
                    view0['maze'].background[newNode.state] = [0,0,0]
                    view0.run()
                else: return solution
                
    return solution
        
                         
        
        
    
            
        
    return None # None is used to indicate no solution



