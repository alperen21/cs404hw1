from Board import Board 
from movement import Movement

def main():
    
    board = Board("board.txt")

    board.print_state()
    print("*************")

    board.move(Movement.LEFT)
    board.print_state()
    print("*************")

    board.move(Movement.RIGHT)
    board.print_state()
    print("*************")

    board.move(Movement.UP)
    board.print_state()
    print("*************")

    board.move(Movement.LEFT)
    board.print_state()
    print("*************")

    board.move(Movement.DOWN)
    board.print_state()
    print("*************")

if __name__ == "__main__":
    main()