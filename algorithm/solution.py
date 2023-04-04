from pprint import pprint
from algorithm.Node import Node

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

