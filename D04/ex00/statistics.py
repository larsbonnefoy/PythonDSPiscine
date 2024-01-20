def ft_statistics(*args, **kwargs) -> None:
    """
    Computes Mean, Median and 25% and 75% Quartile
    """
    input = sorted(list(args))
    assert all(isinstance(item, (float, int)) for item in input), "ERROR"
    nb_val = len(input)
    for v in kwargs.values():
        try:
            assert len(input) != 0, "ERROR"
        except AssertionError as ae:
            print(f"{ae}")
            continue
        match v:
            case "mean":
                print(f"mean : {mean(input)}")
            case "median":
                print(f"median : {input[nb_val // 2]}")
            case "quartile":
                first_q = int(nb_val * 0.25)
                third_q = int(nb_val * 0.75)
                print(f"quartile: {[input[first_q], input[third_q]]}")
            case "std":
                print(f"std: {var(input) ** 0.5}")
            case "var":
                print(f"var: {var(input)}")


def var(input: list) -> float:
    """
    Computes Variance of list given as input
    """
    mean_input = mean(input)
    squared_deviation = [(x - mean_input) ** 2 for x in input]
    return sum(squared_deviation) / len(input)


def mean(input: list) -> float:
    """
    Computes mean of list given as input
    """
    return (sum(input) / len(input))
