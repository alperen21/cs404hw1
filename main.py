from Board import Board 
from movement import Movement

def main():
    
    board = Board("board.txt")

    print(board.predict_colored(Movement.UP))
    for movement in Movement:
        print([movement])
        print(board.predict_colored(movement))



if __name__ == "__main__":
    main()

