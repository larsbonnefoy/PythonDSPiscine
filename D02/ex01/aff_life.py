from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """
    Loads life_expectancy.csv and displays it
    """
    df = load("life_expectancy_years.csv")
    select_contr = df.loc[df['country'] == 'Belgium']
    select_dates = [int(x) for x in df.keys()[1:]]
    plt.plot(select_dates, select_contr.to_numpy()[0][1:])
    plt.title("Belgim Life expectancy Projections")
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.xticks(range(min(select_dates), max(select_dates)+1, 40))
    plt.show()
    second_solution()


def second_solution():
    """
        Other solution to exercice
    """
    df = load("life_expectancy_years.csv")
    country_data = df[df['country'] == 'Belgium']
    # extract data colums exluding 'country'
    # columns returns label of all the colums, we exclude 'country' label
    date_columns = country_data.columns[1:]
    # convert string values to numeric values
    x_values = pd.to_numeric(date_columns)
    # iloc[:, 1:] we take every row (there is only 1 (belgium) => :) and we
    # start at second value (to skip 'Belgium')
    # .values convertes into numpy array
    # .flatten converts into a 1D array
    y_values = country_data.iloc[:, 1:].values.flatten()
    plt.plot(x_values, y_values)
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
