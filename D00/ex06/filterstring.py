import sys
from ft_filter import ft_filter


def main():
    try:
        check_params()
        # Useless list comprehension -> Split can do it directly
        splitList = [word for word in sys.argv[1].split(' ')]
        print(list(ft_filter(lambda x: len(x) > int(sys.argv[2]), splitList)))

    except AssertionError as ae:
        print(f"AssertionError: {ae}")


def check_params():
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    main()
