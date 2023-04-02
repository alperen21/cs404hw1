from Board import Board 
from movement import Movement

def main():
    
    board = Board("board.txt")
    board.print_state()
    board.move(Movement.LEFT)
    board.print_state()

if __name__ == "__main__":
    main()