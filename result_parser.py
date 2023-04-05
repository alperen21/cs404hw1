from os import listdir, path
from os.path import isfile, join
from pprint import pprint 
import re

def parse():

    mypath = "./logs"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    labels = [1,2,3,4,5]
    labels = ["easy"+str(i) for i in labels ] + ["medium"+str(i) for i in labels ] + ["hard"+str(i) for i in labels ]
    labels = ["a-star"+i for i in labels] #+ ["a-star"+i for i in labels]


    results = dict()

    for file in onlyfiles:
        with open(path.join(mypath, file), "r") as f:
            contents = f.read()
            
            memory_regex = "86 *(.*) MiB.*"
            execution_time_regex = "execution took: (.*) s"

            splitted = file.replace(".log", "").split("_")
            label = "".join(splitted)

            

            results[label] = {
                "execution": re.search(execution_time_regex, contents).group(1),
                "memory" : re.findall(memory_regex, contents)[-1]
            }

    for label in labels:
        print(results[label]["execution"], end=" ")






if __name__ == "__main__":
    parse()