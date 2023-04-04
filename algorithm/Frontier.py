from abc import ABC, abstractmethod
from queue import PriorityQueue
from algorithm.Node import Node

class Frontier(ABC):
    """
    Abstract Frontier class, used to implement other frontier implementations 
    by specifying what kind of a data structure to be used (queue, priority queue, stack etc.)
    """
    def __init__(self, data_structure) -> None:
        """
        Constructor for abstract Frontier class

        :param data_structure: what kind of a data structure will be used (queue, priority queue, stack etc.)
        :returns: None
        :raises NoSolutionError: raises an exception if no solution is found
        """
        self.data_structure = data_structure
    
    @abstractmethod
    def put(self, node : Node) -> None:
        """
        Places a node inside of the frontier
        
        :param node: which node is to be placed
        :returns: None
        """
        ... 
    
    @abstractmethod
    def pop(self) -> Node:
        """
        Returns the first element from the frontier in accordance with the data structure used
        
        :returns: Node that is removed from the frontier
        """
        ...
    
    @abstractmethod
    def isEmpty(self) -> bool:
        """
        Checks to see if the Frontier is empty
        
        :returns: boolean value to indicate if the frontier is empty
        """
        ...

class UCS_Frontier(Frontier):
    def __init__(self) -> None:
        """
        Constructor for Uniform Cost Search Frontier class. 
        Constructs the abstract frontier with a priority queue
        
        :returns: Abstract Frontier class
        """
        super().__init__(PriorityQueue())
    
    def put(self, node: Node) -> None:
        """
        Places a node inside of the frontier
        
        :param node: which node is to be placed
        :returns: None
        """
        self.data_structure.put(node)
    
    def pop(self) -> Node:
        """
        Returns the first element from the frontier in accordance with the data structure used
        
        :returns: Node that is removed from the frontier
        """
        return self.data_structure.get()

    def isEmpty(self) -> bool:
        """
        Checks to see if the Frontier is empty
        
        :returns: boolean value to indicate if the frontier is empty
        """
        return self.data_structure.empty()

