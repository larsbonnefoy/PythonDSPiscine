class calculator:
    def __init__(self, lst: list):
        """
        Constructor of calculator class
        """
        self.data = lst

    def __add__(self, object) -> None:
        """
        Addition for calculator class
        """
        self.data = list(map(lambda x: x + object, self.data))
        print(self.data)
        return self.data

    def __mul__(self, object) -> None:
        """
        Multiplication for calculator class
        """
        self.data = list(map(lambda x: x * object, self.data))
        print(self.data)
        return self.data

    def __sub__(self, object) -> None:
        """
        Subtraction for calculator class
        """
        self.data = list(map(lambda x: x - object, self.data))
        print(self.data)
        return self.data

    def __truediv__(self, object) -> None:
        """
        Division for calculator
        """
        try:
            self.data = list(map(lambda x: x / object, self.data))
            print(self.data)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
        return self.data

    def __str__(self):
        return f"{self.data}"
