"""
Returns morse equivalent from string input
1 line sol: print(''.join(NESTED_MORSE[char.upper()] for char in sys.argv[1]))
"""

import sys


def main():
    try:
        assert len(sys.argv) == 2, "The arguments are bad"
        output = ""
        for char in sys.argv[1]:
            assert_char(char)
            string_morse = NESTED_MORSE[char.upper()]
            output += string_morse + " "
        print(output[:-1])
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyError:
        print("AssertionError: The arguments are bad")
    return 0


def assert_char(char):
    if (ord(char) == 32):
        return
    assert (ord("A") <= ord(char.upper()) <= ord("Z")), "The arguments are bad"


NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/ ",
}

if __name__ == "__main__":
    main()
