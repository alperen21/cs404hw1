from abc import ABC, abstractmethod
from queue import PriorityQueue
import copy
from pprint import pprint

class Node:
    def __init__(self, state, cost : int, parent, direction) -> None:
        self.state = state
        self.cost = cost 
        self.parent = copy.deepcopy(parent)

        if (parent != None):
            self.parent.state = copy.deepcopy(parent.state)
        self.direction = direction

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self) -> str:
        state_string = str(self.state).replace("], ", "], \n").replace("\n\n", "\n")
        if self.parent == None:
            return f"cost : {self.cost} \n direction: {self.direction} \n state:\n {state_string}, \n parent :\n None"
        else:
            parent_state_string = str(self.parent.state).replace("], ", "], \n").replace("\n\n", "\n")
            return f"cost : {self.cost} \n direction: {self.direction} \n state:\n {state_string}, \n parent :\n {parent_state_string}"

class Frontier(ABC):
    def __init__(self, data_structure) -> None:
        self.data_structure = data_structure
    
    @abstractmethod
    def put(self, node : Node) -> None:
        ... 
    
    @abstractmethod
    def pop(self) -> Node:
        ...
    
    @abstractmethod
    def isEmpty(self) -> bool:
        ...

class UCS_Frontier(Frontier):
    def __init__(self) -> None:
        super().__init__(PriorityQueue())
    
    def put(self, node: Node) -> None:
        self.data_structure.put(node)
    
    def pop(self) -> Node:
        return self.data_structure.get()

    def isEmpty(self) -> bool:
        return self.data_structure.empty()

def solution(initial_node : Node, goal_node : Node) -> None:
    pprint(initial_node.state.state)
    print("---------------------")
    solution_helper(goal_node)

def solution_helper(goal_node : Node) -> None:
    if goal_node.parent == None:
        return
    solution_helper(goal_node.parent)
    pprint(goal_node.state.state)
    print("---------------------")