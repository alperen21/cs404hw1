import pprint
import numpy as np
from movement import Movement

class Action():
    def __init__(self, movement : Movement, cost : int) -> None:
        self.movement = movement
        self.cost = cost
    
    def __repr__(self) -> str:
        return f"movement {self.movement} cost {self.cost}"

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
    
    def get_actions(self):
        actions = list()
        for movement in Movement:
            cost = self.cost(movement)
            actions.append(Action(movement, cost))
        return actions

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
    def predict_colored(self, movement):
        counter = 0
        if movement == Movement.RIGHT:
            for col_no, elem in enumerate(self.state[self.agent.row][self.agent.col:], self.agent.col):
                if elem == "X":
                    break
                if elem == "0":
                    counter += 1
            
        elif movement == Movement.LEFT:

            current_row = list(enumerate(self.state[self.agent.row]))
            current_row = current_row[:self.agent.col + 1]

            for  col_no, elem in reversed(current_row):
                if elem == "X":
                    break
                if elem == "0":
                    counter += 1

        elif movement == Movement.DOWN:
            self.transpose_state()
            counter = self.predict_colored(Movement.RIGHT)
            self.transpose_state()
        
        elif movement == Movement.UP:
            self.transpose_state()
            counter = self.predict_colored(Movement.LEFT)
            self.transpose_state()
        
        return counter
    def move(self, movement):
        if movement == Movement.RIGHT:
            for col_no, elem in enumerate(self.state[self.agent.row][self.agent.col:], self.agent.col):
                
                if elem == "X":
                    self.state[self.agent.row][col_no - 1] = "S"
                    self.agent.row = self.agent.row
                    self.agent.col = col_no - 1
                    break

                self.state[self.agent.row][col_no] = "1"

                if col_no == len(self.state[self.agent.row]) - 1: #if it is in the edge of the board
                    self.state[self.agent.row][col_no] = "S"
                    self.agent.row = self.agent.row
                    self.agent.col = col_no
            
        elif movement == Movement.LEFT:

            current_row = list(enumerate(self.state[self.agent.row]))
            current_row = current_row[:self.agent.col + 1]

            
            for  col_no, elem in reversed(current_row):
                if elem == "X":
                    self.state[self.agent.row][col_no + 1] = "S"
                    self.agent.row = self.agent.row
                    self.agent.col = col_no + 1
                    break
                
                self.state[self.agent.row][col_no] = "1"

                if col_no == 0: #if it is in the edge of the board
                    self.state[self.agent.row][col_no] = "S"
                    self.agent.row = self.agent.row
                    self.agent.col = col_no

        elif movement == Movement.DOWN:
            self.transpose_state()
            self.move(Movement.RIGHT)
            self.transpose_state()
        
        elif movement == Movement.UP:
            self.transpose_state()
            self.move(Movement.LEFT)
            self.transpose_state()
    def transpose_state(self):
        self.state = np.array(self.state).transpose().tolist()
        temp = self.agent.col
        self.agent.col = self.agent.row
        self.agent.row = temp
    def cost(self, movement):
        
        if movement == Movement.LEFT or movement == Movement.RIGHT:
            return len(self.state[0]) - self.predict_colored(movement)
        else:
            return len(self.state) - self.predict_colored(movement) 
    def goal_test(self):
        for row in self.state:
            for elem in row:
                if elem == 0:
                    return False
        return True
