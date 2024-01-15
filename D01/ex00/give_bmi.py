"""
Body mass index (BMI) is a value derived from the mass (weight) and height of a
person. The BMI is defined as the body mass divided by the square of the body
height, and is expressed in units of kg/m2, resulting from mass in kilograms
(kg) and height in metres (m).
"""

import numpy as np


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """
    Takes list of height and weight and returns bmi index
    Handle errors: if input lists are not same size, are not int or float
    """
    try:
        assert len(h) == len(w), "Lenght are not the same"
        check_type(h)
        check_type(w)
        return list(np.array(w) / (np.array(h) ** 2))
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
    return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Set value in list to True if value is above limit, false otherwise
    """
    return list(map(lambda x: x > limit, bmi))


def check_type(lst: list):
    """
        Checks if all types in the list passed as parameters are either floats
        or ints
    """
    if not all(isinstance(item, (float, int)) for item in lst):
        raise ValueError("Items in list are not float or int")
