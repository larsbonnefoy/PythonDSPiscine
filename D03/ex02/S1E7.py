from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family
    """

    def __init__(self, name: str, alive=True):
        """
        Constructor Baratheon class
        """
        self.name = name
        self.is_alive = alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Converts class to string
        """
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        String Representation of Baratheon class
        """
        return self.__str__()

    def set_eyes(self, color: str):
        """
        Sets color of eyes
        """
        self.eyes = color

    def set_hairs(self, color: str):
        """
        Sets color of hairs
        """
        self.hairs = color

    def get_eyes(self):
        """
        Sets color of eyes
        """
        return self.eyes

    def get_hairs(self):
        """
        Sets color of hairs
        """
        return self.hairs

    def abstract_method():
        pass


class Lannister(Character):
    """
    Representing the Lanister family
    """

    def __init__(self, name: str, alive=True):
        self.first_name = name
        self.is_alive = alive
        self.family_name = "Lanister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, name: str, alive=True):
        """
        Class method that enables creation from class
        """
        return Lannister(name, alive)

    def __str__(self):
        """
        Converts class to string
        """
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        String Representation of Lannister class
        """
        return self.__str__()

    def abstract_method():
        pass
