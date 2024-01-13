"""
takes a single string argument and displays the sums of its upper-case
characters, lower-case characters, punctuation characters, digits and spaces.
"""

import sys


def main():
    """
    Main of building.py
    """
    try:
        string_to_parse = get_input_string()
        upper = 0
        lower = 0
        punctuation = 0
        space = 0
        digit = 0
        for character in string_to_parse:
            if ord("A") <= ord(character) <= ord("Z"):
                upper = upper + 1
            elif ord("a") <= ord(character) <= ord("z"):
                lower = lower + 1
            elif ord("0") <= ord(character) <= ord("9"):
                digit = digit + 1
            elif ord(character) == 32:
                space = space + 1
            elif is_punctuation(character):
                punctuation = punctuation + 1
        sum = multi_sum(upper, lower, punctuation, space, digit)
        print(
            "The text contains "
            + str(sum)
            + "characters:\n"
            + str(upper)
            + "upper letters"
            + str(lower)
            + "upper letters"
            + str(punctuation)
            + "punctuation mark"
            + str(space)
            + "spaces"
            + str(digit)
            + "digits"
        )
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return 1


def multi_sum(*args):
    """
    Sums multiple arguments
    """
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum


def is_punctuation(char):
    """
    Checks if character is a punctuation mark
    """
    return (
        33 <= ord(char) <= 47
        or 58 <= ord(char) <= 64
        or 91 <= ord(char) <= 96
        or 123 <= ord(char) <= 126
    )


def get_input_string() -> str:
    """
    Returns input to parse.
    If argument is provided returns argument.
    If no argument is provided prompts user to given an argument
    If more than 1 argument is provided throws an error
    """
    match len(sys.argv):
        case 1:
            input_string = input("What is the text to count?\n")
        case 2:
            input_string = sys.argv[1]
        case _:
            raise AssertionError("more than one argumet is provided")
    return input_string


if __name__ == "__main__":
    main()
