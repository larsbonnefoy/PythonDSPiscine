"""
The function must copy the function tqdm with the yield operator.
"""


def ft_tqdm(lst: range) -> None:
    num = lst.start
    nb_bar = 64
    while True:
        progress = (num - lst.start) / (lst.stop - lst.start)
        bar = "=" * int(progress * nb_bar)\
            + " " * int((1 - progress) * nb_bar)\
            + ">"
        print(f"{int(progress * 100)}%|[{bar}]| {num}/{lst.stop}", end="\r")
        num += lst.step
        if num > lst.stop:
            break
        yield num
