import subprocess
import re
from pprint import pprint


def run(algorithm : str, difficulty : str) -> float:
    process = subprocess.run(f"time python main.py --difficulty {difficulty} --algorithm {algorithm}".split(" "), capture_output=True, text=True)
    stdout = process.stdout
    execution_time_regex = re.search("execution took: (.*) s", stdout)
    memory_regex = re.search("75 *(.*) MiB.*", stdout)
    return {
        "time": execution_time_regex.group(1),
        "memory": memory_regex.group(1)
    }



def main():
    algorithms = reversed(["ucs", "a_star"])
    difficulties = ["easy", "medium", "hard"]
   
    results = dict()

    for algorithm in algorithms:
       results[algorithm] = dict()
       for difficulty in difficulties:
           results[algorithm][difficulty] = run(algorithm, difficulty)
    
    pprint(results)


if __name__ == "__main__":
    main()