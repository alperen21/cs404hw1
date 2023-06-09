from algorithm.Frontier import UCS_Frontier
from algorithm.Node import Node
from algorithm.solution import solution
from board.Board import Board
from board.SUCC_H import SUCC_H
from exceptions.NoSolution import NoSolutionError


def a_star(filename) -> None:
    """
    A* search implementation

    :param filename: name of the file
    :raises NoSolutionError: raises an exception if no solution is found
    :returns: None
    """
    closed = list()
    frontier = UCS_Frontier()

    start = Board()
    start.read_file(filename)
    initial_node = Node(
        start,
        0,
        None,
        None
    )
    frontier.put(initial_node)

    while not frontier.isEmpty():
        n = frontier.pop()

        if n.state.goal_test():
            solution(initial_node, n)
            print("distance traveled:", n.state.distance)
            print("number of expanded nodes:", len(closed))
            return

        for s in SUCC_H(n):
            s.cost += n.cost

            if s.state not in [
                    elem.state for elem in frontier.data_structure.queue] and s.state not in [
                    elem.state for elem in closed]:
                frontier.put(s)

            temp = list()
            while (not frontier.isEmpty()):
                popped = frontier.pop()
                if (s.state.state == popped.state.state and s.cost < popped.cost):
                    popped.cost = s.cost
                    popped.parent = n
                temp.append(popped)

            for elem in temp:
                frontier.put(elem)

        closed.append(n)

    raise NoSolutionError