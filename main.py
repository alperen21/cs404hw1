from algorithm.ucs import ucs
from algorithm.a_star import a_star
import argparse
import time
from board.Board import Board
from board.SUCC import SUCC
from algorithm.movement import Movement
from algorithm.Node import Node
from memory_profiler import profile


def start_ucs(difficulty : str, start : int, end : int) -> None:
    """
    Runs UCS over the selected difficulty

    :param difficulty: difficulty level
    :param start: start of the range of matrices
    :param difficulty: end of the range of matrices
    :returns: None
    """
    for i in range(start,end):
        ucs(f"inputs/{difficulty}/{difficulty}{i}.txt")

def start_a_star(difficulty : str, start : int, end : int) -> None:
    """
    Runs A* search over the selected difficulty

    :param difficulty: difficulty level
    :param start: start of the range of matrices
    :param difficulty: end of the range of matrices
    :returns: None
    """
    for i in range(start,end):
        a_star(f"inputs/{difficulty}/{difficulty}{i}.txt")

@profile(precision=4)
def main() -> None:    
    """
    The main function

    :returns: None
    """
    start = time.time()

    parser = argparse.ArgumentParser(description='Use a search function to solve maze coloring problem')
    parser.add_argument('--difficulty', type=str, required=True)
    parser.add_argument('--algorithm', type=str, required=True)
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--end', type=int, required=True)

    args = parser.parse_args()
    
    if args.algorithm == "ucs":
        if args.difficulty == "easy":
            print("using ucs with easy")
            start_ucs("easy", args.start, args.end)

        elif args.difficulty == "medium":
            print("using ucs with medium")
            start_ucs("medium", args.start, args.end)

        elif args.difficulty == "hard":
            print("using ucs with hard")
            start_ucs("hard", args.start, args.end)
        else:
            parser.print_help()
            
    elif args.algorithm == "a_star":
        if args.difficulty == "easy":
            print("using A* with easy")
            start_a_star("easy", args.start, args.end)

        elif args.difficulty == "medium":
            print("using A* with medium")
            start_a_star("medium", args.start, args.end)

        elif args.difficulty == "hard":
            print("using A* with hard")
            start_a_star("hard", args.start, args.end)
        else:
            parser.print_help()
    else:
        parser.print_help()
    end = time.time()

    print(f"execution took: {end - start} s")

if __name__ == "__main__":
    main()
