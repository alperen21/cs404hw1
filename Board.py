import pprint
from movement import Movement


class Agent():
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

class Board():
    def __init__(self, filename):

        self.state = list()
        with open(filename, "r") as file:
            for line in file.readlines():
                self.state.append(line.strip().split(", "))
        agent_coordiantes = self.find_agent()
        self.agent = Agent(agent_coordiantes[0], agent_coordiantes[1])
        
    def find_agent(self):
        for row_num, row in enumerate(self.state):
            for col_num, element in enumerate(row):
                if element == "S":
                    assert self.state[row_num][col_num] == "S"
                    return (row_num, col_num)
        raise Exception("S not found")

    def print_state(self):
        pprint.pprint(self.state)
        print(f"the agent is in row {self.agent.row} and col {self.agent.col}")

    def move(self, movement):
        if movement == Movement.RIGHT:
            for col_no, elem in enumerate(self.state[self.agent.row][self.agent.col:], self.agent.col):
                
                if elem == "X":
                    self.state[self.agent.row][col_no - 1] = "S"
                    break

                self.state[self.agent.row][col_no] = "1"

                if col_no == len(self.state[self.agent.row]) - 1: #if it is in the edge of the board
                    self.state[self.agent.row][col_no] = "S"
            
        elif movement == Movement.LEFT:

            current_row = list(enumerate(self.state[self.agent.row]))
            current_row = current_row[:self.agent.col + 1]

            
            for  col_no, elem in reversed(current_row):
                if elem == "X":
                    self.state[self.agent.row][col_no + 1] = "S"
                    break
                
                self.state[self.agent.row][col_no] = "1"

                if col_no == 0: #if it is in the edge of the board
                    self.state[self.agent.row][col_no] = "S"





            

    def cost(self, action):
        pass

    def goal_test(self):
        pass
