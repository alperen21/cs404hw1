import copy

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
