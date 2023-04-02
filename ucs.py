from Board import Board, successor

def ucs():
    closed = list()
    start_node = Board("board.txt")

    frontier = list()
    frontier.append([0, start_node])

    while len(frontier) > 0:
        frontier = sorted(frontier, key=lambda x: x[0], reverse=True)
        node = frontier.pop()

        if node[1].goal_test():
            node[1].print_state()
            return
        
        successors = successor(node[1])

        for s in successors:
            s[0] += node[0]

            if s[1] not in [elem[1] for elem in closed] and s[1] not in [elem[1] for elem in frontier]:
                frontier.append(s)

            for elem in frontier:
                if (s[1] == elem[1]):
                    if s[0] > elem[0]:
                        elem[0] = s[0]

        closed.append(node)
                