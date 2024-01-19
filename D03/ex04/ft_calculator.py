
class calculator:
    """
    calculator class doing dot, addition and subtraction of vectors
    """

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """
        Dot product between v1 and v2
        """
        ret = sum(list(map(lambda x, y: x * y, V1, V2)))
        print(ret)
        return ret

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
        Addition of two vectors
        """
        ret = list(map(lambda x, y: x + y, V1, V2))
        print(ret)
        return ret

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
            subtraction of two vectors
            Zip creates a tuple x,y where x is ith value of V1 and y ith value
            of V2
        """
        ret = [tp[0] - tp[1] for tp in zip(V1, V2)]
        print(ret)
        return ret
