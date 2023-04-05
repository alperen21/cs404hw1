from pprint import pprint
from algorithm.Node import Node


def solution(initial_node: Node, goal_node: Node) -> None:
    """
    Prints the solution

    :param initial_node: the starting node
    :param goal_node: the node that passes the goal test
    :returns: None
    """
    print("---------------------")
    pprint(initial_node.state.state)
    solution_helper(goal_node)
    


def solution_helper(goal_node: Node) -> None:
    """
    Recursive helper function of solution function

    :param goal_node: the node that passes the goal test
    :returns: None
    """
    if goal_node.parent is None:
        return
    solution_helper(goal_node.parent)
    pprint(goal_node.state.state)
    print("---------------------")
