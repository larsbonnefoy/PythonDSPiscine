from array2D import slice_me


def main():
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    family1 = [[1.80, 78.4, 14.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    family2 = [[1.80], [2.15], [2.10], [1.88]]
    family3 = "salut"
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print(slice_me(family1, 0, 2))
    print(slice_me(family2, 0, 2))
    print(slice_me(family3, 0, 2))


if __name__ == "__main__":
    main()
