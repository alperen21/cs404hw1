import pprint
import numpy as np
from algorithm.movement import Movement
import copy
from algorithm.Frontier import Node
from board.agent import Agent


class Board():
    """
    Board class to indicate the current state
    """

    def __init__(self) -> None:
        """
        Constructor for the board class
        :returns: None
        """
        self.state = list()

    def read_file(self, filename: str) -> None:
        """
        Reads file to construct a matrix representation of the file

        :param filename: name of the file
        :returns: None
        """
        with open(filename, "r") as file:
            for line in file.readlines():
                self.state.append(line.strip().split(", "))
        agent_coordiantes = self.find_agent()
        self.agent = Agent(agent_coordiantes[0], agent_coordiantes[1])

    def __str__(self) -> str:
        """
        Board class overrides __str__ to print meaningful information when printed

        :returns: string representation
        """
        return str(self.state).replace("], ", "], \n")

    def find_agent(self) -> None:
        """
        Finds the coordinates of the agent

        :raises Exception: raises an exception if there is no agent
        :returns: None
        """
        for row_num, row in enumerate(self.state):
            for col_num, element in enumerate(row):
                if element == "S":
                    assert self.state[row_num][col_num] == "S"
                    return (row_num, col_num)
        raise Exception("S not found")

    def print_state(self) -> None:
        """
        Prints information about the state and the agent

        :returns: None
        """
        pprint.pprint(self.state)
        print(f"the agent is in row {self.agent.row} and col {self.agent.col}")

    def predict_colored(self, movement: Movement) -> int:
        """
        Predicts how many grids will be colored by the move

        :param movement: to which cardinal direction the agent is to move
        :returns: how many grids will be colored by the move
        """
        counter = 0
        if movement == Movement.RIGHT:
            for col_no, elem in enumerate(
                    self.state[self.agent.row][self.agent.col:], self.agent.col):
                if elem == "X":
                    break
                if elem == "0":
                    counter += 1

        elif movement == Movement.LEFT:

            current_row = list(enumerate(self.state[self.agent.row]))
            current_row = current_row[:self.agent.col + 1]

            for col_no, elem in reversed(current_row):
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

    def move(self, movement) -> None:
        """
        Moves the agent to the specified direction

        :param movement: to which cardinal direction the agent is to move
        :returns: None
        """
        if movement == Movement.RIGHT:
            for col_no, elem in enumerate(
                    self.state[self.agent.row][self.agent.col:], self.agent.col):

                if elem == "X":
                    self.state[self.agent.row][col_no - 1] = "S"
                    self.agent.row = self.agent.row
                    self.agent.col = col_no - 1
                    break

                self.state[self.agent.row][col_no] = "1"

                if col_no == len(
                        self.state[self.agent.row]) - 1:  # if it is in the edge of the board
                    self.state[self.agent.row][col_no] = "S"
                    self.agent.row = self.agent.row
                    self.agent.col = col_no

        elif movement == Movement.LEFT:

            current_row = list(enumerate(self.state[self.agent.row]))
            current_row = current_row[:self.agent.col + 1]

            for col_no, elem in reversed(current_row):
                if elem == "X":
                    self.state[self.agent.row][col_no + 1] = "S"
                    self.agent.row = self.agent.row
                    self.agent.col = col_no + 1
                    break

                self.state[self.agent.row][col_no] = "1"

                if col_no == 0:  # if it is in the edge of the board
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

    def get_board(self) -> list[list[str]]:
        """
        Returns a deep copy of the matrix used to denote the maze

        :returns: deep copy of the matrix used to denote the maze
        """
        new_board = self.__init__()
        new_board.state = copy.deepcopy(self.state)
        new_board.agent = copy.deepcopy(self.agent)
        return new_board

    def transpose_state(self) -> None:
        """
        Transposes the matrix used to denote the board

        :returns: None
        """
        self.state = np.array(self.state).transpose().tolist()
        temp = self.agent.col
        self.agent.col = self.agent.row
        self.agent.row = temp

    def cost(self, movement) -> int:
        """
        The cost function

        :param movement: to which cardinal direction the agent is to move
        :returns: the cost of moving to that direction
        """
        if movement == Movement.LEFT or movement == Movement.RIGHT:
            return len(self.state[0]) - self.predict_colored(movement)
        else:
            return len(self.state) - self.predict_colored(movement)

    def heuristic(self, movement) -> int:
        """
        Heuristic function

        :param movement: to which cardinal direction the agent is to move
        :returns: Returns the heuristic value of moving to that direction
        """
        return 0

    def goal_test(self):
        """
        Goal test, works by checking if there are no 0's in the matrix

        :returns: if the goal is met
        """
        for row in self.state:
            for elem in row:
                if elem == "0":
                    return False
        return True

    def __eq__(self, __value: object) -> bool:
        """
        == operator overloading

        :param __value: the value this board is being compared to
        :returns: If two objects are equivalent
        """
        return self.state == __value.state
