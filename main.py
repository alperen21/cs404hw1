from Board import Board, successor
from pprint import pprint
from movement import Movement

def main():
    
    board = Board("board.txt")
    successors = successor(board)

    for succ in successors:
        print("cost of successor:", succ[0])
        succ[1].print_state()



if __name__ == "__main__":
    main()

