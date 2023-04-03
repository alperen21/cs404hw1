from Board import Board, SUCC
from pprint import pprint
from movement import Movement
from queue import PriorityQueue
from Algorithms import Node
from ucs import ucs
import copy
from pprint import pprint




def main():
    ucs()
    # board = Board()
    # board.read_file("board.txt")

    # parent = Node(
    #     board,
    #     0,
    #     None,
    #     None
    # )
    
    

    # parent_clone = copy.deepcopy(parent)
    # parent_clone.state.move(Movement.LEFT)
    # child1 = Node(
    #     parent_clone.state,
    #     0,
    #     parent,
    #     Movement.LEFT
    # )

    # child1_clone = copy.deepcopy(child1)
    # child1_clone.parent = parent
    # child1_clone.state.move(Movement.UP)


    # child2 = Node(
    #     child1_clone.state,
    #     0,
    #     child1_clone,
    #     Movement.UP
    # )

    # print(child2.parent.parent.state)
    # print("************")
    # print(child2.parent.state)
    # print("************")
    # print(child2.state)
    

 




    


    

    

if __name__ == "__main__":
    main()

