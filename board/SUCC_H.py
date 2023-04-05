import copy
from algorithm.Node import Node
from algorithm.movement import Movement


def SUCC_H(node: Node) -> list[Node]:
    """
    Successor function that also takes into account the heuristic function

    :param node: the parent node
    :returns: Successors of the parent node
    """
    children = list()

    for movement in Movement:
        child = copy.deepcopy(node)

        child.cost = child.state.cost(
            movement) + child.state.heuristic(movement)

        child.state.move(movement)

        child.parent = node

        child.direction = movement

        child.state.distance += node.state.distance

        children.append(child)

    return children
