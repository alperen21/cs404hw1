from algorithm.Node import Node
from algorithm.movement import Movement
import copy

def SUCC(node : Node) -> list[Node]:
    """
    Successor function

    :param node: the parent node
    :returns: Successors of the parent node
    """   
    children = list()

    for movement in Movement:
        child = copy.deepcopy(node)

        child.cost = child.state.cost(movement)

        child.state.move(movement)

        child.parent = node

        child.direction = movement

        children.append(child)
    
    return children
