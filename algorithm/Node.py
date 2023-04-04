import copy

class Node:
    """
    Node Class to indicate a single node in any of the search algorithms
    """
    def __init__(self, state, cost : int, parent, direction) -> None:
        """
        Node constructor
        
        :param state: the board class to indicate the state of the maze
        :param cost: the cost of the state when it is accessed from the parent
        :param parent: parent of the node
        :param direction: which direction is to be selected to reach from the parent node to this node
        :returns: None
        """
        self.state = state
        self.cost = cost 
        self.parent = copy.deepcopy(parent)

        if (parent != None): # if parent is none, it means this is the first node
            self.parent.state = copy.deepcopy(parent.state)
        self.direction = direction

    def __lt__(self, other) -> bool:
        """
        Node overrides comparison operators so that it can be used in Python's native PriorityQueue implementation
        
        :param other: the node this node is being compared to
        :returns: Boolean value to indicate if this node is smaller or not
        """
        return self.cost < other.cost

    def __repr__(self) -> str:
        """
        Node overrides __repr__ so that when it is printed, it prints meaningful information and not just address of the object

        :returns: string representation
        """
        state_string = str(self.state).replace("], ", "], \n").replace("\n\n", "\n") # this is done for better matrix representation
        if self.parent == None: # checks if this is the initial node to avoid exception
            return f"cost : {self.cost} \n direction: {self.direction} \n state:\n {state_string}, \n parent :\n None"
        else:
            parent_state_string = str(self.parent.state).replace("], ", "], \n").replace("\n\n", "\n")
            return f"cost : {self.cost} \n direction: {self.direction} \n state:\n {state_string}, \n parent :\n {parent_state_string}"
