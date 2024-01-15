import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Prints shape of 2D array and truncate the list on provided start and
        end argument
        list: is a 2D array -> check for dimensions, check if homogenous
    """
    try:
        assert isinstance(family, list), "Is not of type list"
        array2D = np.array(family)
        assert np.shape(array2D)[1] == 2, "Is not a two dimensionnal array"
        print("My shape is : " + str(np.shape(array2D)))
        reshaped = array2D[start: end]
        print("My new shape is : " + str(np.shape(reshaped)))
        return (reshaped.tolist())
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
    return []
