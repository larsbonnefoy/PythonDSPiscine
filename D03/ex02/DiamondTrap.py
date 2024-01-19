from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing a King
    """

    def __init__(self, name, is_alive=True):
        """
        Constructor of King Class. Takes by default values from Baratheon
        -> First argument passed
        """
        super().__init__(name, is_alive)
