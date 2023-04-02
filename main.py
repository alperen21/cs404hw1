from Board import Board, successor
from pprint import pprint
from movement import Movement

def main():
    
    board = Board("board.txt")
    print(board.goal_test())

    

    

if __name__ == "__main__":
    main()

