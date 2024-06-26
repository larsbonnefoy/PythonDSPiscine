"""
takes a single string argument and displays the sums of its upper-case
characters, lower-case characters, punctuation characters, digits and spaces.
"""

from sys import argv


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
            if character.isupper():
                upper += 1
            elif character.islower():
                lower += 1
            elif character.isdigit():
                digit += 1
            elif character == ' ':
                space += 1
            elif is_punctuation(character):
                punctuation += 1
        sum = len(string_to_parse)
        print(
            "The text contains "
            + str(sum)
            + " characters:\n"
            + str(upper)
            + " upper letters\n"
            + str(lower)
            + " lower letters\n"
            + str(punctuation)
            + " punctuation mark\n"
            + str(space)
            + " spaces\n"
            + str(digit)
            + " digits"
        )
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    except EOFError:
        return 1
    return 0


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
    match len(argv):
        case 1:
            input_string = input("What is the text to count?\n")
        case 2:
            input_string = argv[1]
        case _:
            raise AssertionError("more than one argumet is provided")
    return input_string


if __name__ == "__main__":
    main()
