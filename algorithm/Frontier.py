from abc import ABC, abstractmethod
from queue import PriorityQueue
from algorithm.Node import Node

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

