from ft_filter import ft_filter


def greater(x):
    if x > 2:
        return True
    return False


def main():
    myList = [0, 1, 2, 3]
    mySet = {1, 2, 3}
    myDict = {1: "3", 2: "2", 3: "1"}

    try:
        assert list(filter(greater, myList)) == list(
            ft_filter(greater, myList)
        ), "Lists are not equal"
        assert list(filter(None, myList)) == list(
            ft_filter(None, myList)
        ), "Lists are not equal"
        assert set(filter(greater, mySet)) == set(
            ft_filter(greater, mySet)
        ), "Sets are not equal"
        fdict = dict(filter(lambda item: int(item[1]) > 2, myDict.items()))
        ft_dict = dict(ft_filter(lambda x: int(x[1]) > 2, myDict.items()))
        assert fdict == ft_dict, "Dicts are not equal"
        print(fdict)
        print(ft_dict)
        print(list(filter(None, myList)))
        print(list(ft_filter(None, myList)))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
