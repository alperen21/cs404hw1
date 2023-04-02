from Board import Board 
from pprint import pprint
from movement import Movement

def main():
    
    board = Board("board.txt")

    pprint(board.get_actions())



if __name__ == "__main__":
    main()

