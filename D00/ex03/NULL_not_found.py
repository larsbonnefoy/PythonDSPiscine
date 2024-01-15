"""
Write a function that prints the object type of all types of "Null".
Return 0 if it goes well and 1 in case of error.
Your function needs to print all types of NULL
"""


def NULL_not_found(object: any) -> int:
    if (is_nan(object)):
        print("Cheese: " + str(object) + " " + str(type(object)))
        return 0
    match object:
        case None:
            print("Nothing: " + str(object) + " " + str(type(object)))
            return 0
        case False:
            print("Fake: " + str(object) + " " + str(type(object)))
            return 0
        case 0:
            print("Zero: " + str(object) + " " + str(type(object)))
            return 0
        case '':
            print("Empty: " + str(object) + " " + str(type(object)))
            return 0
        case _:
            print("Type not Found")
            return 1


def is_nan(val):
    return val != val
