from abc import ABC, abstractmethod
# abc = abstract base class


class Character(ABC):
    """
    Abstract Character class
    """

    def __init__(self, name: str, alive=True):
        """
        Constructor called by concrete class
        """
        self.name = name
        self.is_alive = alive

    def die(self):
        """
        Changes value from is_alive to False

        """
        self.is_alive = False

    @abstractmethod
    def abstract_method():
        pass


class Stark(Character):
    """
    Concrete implementation of abstract Character class
    """

    def __init__(self, name: str, alive=True):
        """
        Initalization of Concrete Stark class. Calls Constructor of
        super class
        """
        super().__init__(name, alive)

    def abstract_method():
        pass
