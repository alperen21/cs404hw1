import pprint

class Board():
    def __init__(self, filename : str) -> None:

        self.state = list()
        with open(filename, "r") as file:
            for line in file.readlines():
                self.state.append(line.strip().split(", "))
        
    def print_state(self):
        pprint.pprint(self.state)

    def move_right(self):
        pass

    def move_left(self):
        pass 

    def move_up(self):
        pass

    def move_down(self):
        pass

    def cost(self, action):
        pass

    def goal_test(self):
        pass
