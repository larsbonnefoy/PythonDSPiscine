from load_csv import load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = load("population_total.csv")
    x_val = pd.to_numeric(df.columns[1:])
    data = df[(df['country'] == 'France') | (df['country'] == 'Belgium')]
    select_cols = data.iloc[:, 1:].values
    converted_data = np.vectorize(convert)(select_cols)
    plt.plot(x_val, converted_data[0], label="Belgium", color='Blue')
    plt.plot(x_val, converted_data[1], label="France", color='Green')
    plt.title("Population Projections")
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xlim(1800, 2050)
    plt.xticks(range(1800, 2050, 40))
    plt.yticks([20000000, 40000000, 60000000], ['20M', '40M', '60M'])
    plt.legend(loc='lower right')
    plt.show()
    return 0


def convert(inputString):
    unit = {"M": 1000000,
            "k": 1000
            }
    unitVal = inputString[-1]
    return (float(inputString[:-1]) * float(unit[unitVal]))


if __name__ == "__main__":
    main()
