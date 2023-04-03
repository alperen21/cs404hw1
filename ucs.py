from Algorithms import UCS_Frontier, Node, solution
from Board import Board, SUCC

def ucs():
    closed = list()
    frontier = UCS_Frontier()
    
    start = Board()
    start.read_file("board.txt")
    initial_node = Node(
        start,
        0,
        None,
        None
    )
    frontier.put(initial_node)

    while not frontier.isEmpty():
        n = frontier.pop()
        
        if n.state.goal_test():
            solution(initial_node, n)
            return
        
        for s in SUCC(n):
            s.cost += n.cost
        
            if s.state not in [elem.state for elem in frontier.data_structure.queue] and s.state not in [elem.state for elem in closed]:
                frontier.put(s)

            temp = list()  
            while(not frontier.isEmpty()):
                popped = frontier.pop()
                if (s.state == popped.state and s.cost < popped.cost):
                    popped.cost = s.cost
                    popped.parent = n
                temp.append(popped)
            
            for elem in temp:
                frontier.put(elem)
        
        closed.append(n)
            

            
            
        