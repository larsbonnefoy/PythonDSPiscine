"""
Body mass index (BMI) is a value derived from the mass (weight) and height of a
person. The BMI is defined as the body mass divided by the square of the body
height, and is expressed in units of kg/m2, resulting from mass in kilograms
(kg) and height in metres (m).
"""

import numpy as np


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = list(give_bmi(height, weight))
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """
    Takes list of height and weight and returns bmi index
    Handle errors: if input lists are not same size, are not int or float
    """
    assert len(h) == len(w), "Lenght are not the same"
    check_type(h)
    check_type(w)
    return np.array(w) / (np.array(h) ** 2)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return list(map(lambda x: x > limit, bmi))


def check_type(lst: list):
    if not all(isinstance(item, (float, int)) for item in lst):
        raise ValueError("Items in list are not float or int")


if __name__ == "__main__":
    main()
