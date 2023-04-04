class Agent():
    """
    Class used to indicate the coordinates of the agent    
    """
    def __init__(self, row, col) -> None:
        """
        Constructor for the agent class

        :param row: the row in which the agent is located at
        :param col: the col in which the agent is located at
        :returns: None
        """
        self.row = row
        self.col = col