from algorithm.ucs import ucs
from algorithm.a_star import a_star
import argparse
import time
from memory_profiler import profile


def start_ucs(difficulty : str) -> None:
    """
    Runs UCS over the selected difficulty

    :param difficulty: difficulty level
    :returns: None
    """
    for i in range(1,6):
        ucs(f"inputs/{difficulty}/{difficulty}{i}.txt")

def start_a_star(difficulty : str) -> None:
    """
    Runs A* search over the selected difficulty

    :param difficulty: difficulty level
    :returns: None
    """
    for i in range(1,6):
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
    args = parser.parse_args()
    
    if args.algorithm == "ucs":
        if args.difficulty == "easy":
            print("using ucs with easy")
            start_ucs("easy")

        elif args.difficulty == "medium":
            print("using ucs with medium")
            start_ucs("medium")

        elif args.difficulty == "hard":
            print("using ucs with hard")
            start_ucs("hard")
        else:
            parser.print_help()
            
    elif args.algorithm == "a_star":
        if args.difficulty == "easy":
            print("using A* with easy")
            start_a_star("easy")

        elif args.difficulty == "medium":
            print("using A* with medium")
            start_a_star("medium")

        elif args.difficulty == "hard":
            print("using A* with hard")
            start_a_star("hard")
        else:
            parser.print_help()
    else:
        parser.print_help()
    end = time.time()

    print(f"execution took: {end - start} s")

if __name__ == "__main__":
    main()
