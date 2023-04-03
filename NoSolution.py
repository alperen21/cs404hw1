class NoSolutionError(Exception):
    """Exception raised when no exceptions.
    """

    def __init__(self,):
        self.message = "This maze has no solutions"
        super().__init__(self.message)