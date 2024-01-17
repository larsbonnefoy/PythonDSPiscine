from load_csv import load


def main():
    print(load("0"))
    print(load("1"))
    print(load("./life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
