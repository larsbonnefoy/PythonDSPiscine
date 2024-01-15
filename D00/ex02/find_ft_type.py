"""
Write a function that prints the object type and returns 42

def all_thing_is_obj(object: any) -> int:
"""


def all_thing_is_obj(object: any) -> int:
    if type(object) is str:
        print(f"{object} is in the kitchen : " + str(type(object)))
    elif type(object) is dict:
        print("Dict : " + str(type(object)))
    elif type(object) is set:
        print("Set : " + str(type(object)))
    elif type(object) is list:
        print("List : " + str(type(object)))
    elif type(object) is tuple:
        print("Tuple : " + str(type(object)))
    else:
        print("Type not found")
    return 42
