from Board import Board

class UCS():
    def __init__(self) -> None:
        self.closed = list()
        self.frontier = list()

    def run(self):
        self.closed = list() #closed is empty
        self.frontier = list() #closed is empty
        
        initial_state = Board("board.txt")
        self.frontier.append(initial_state)

        while len(self.frontier) != 0:
            pass