from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life_expect = load("life_expectancy_years.csv")
    year = "1900"
    df_income_year = df_income[year].values
    df_life_expect_year = df_life_expect[year].values
    plt.scatter(df_income_year, df_life_expect_year)
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.ylabel('Life Expectancy')
    plt.xlabel('Gross domestic product')
    plt.title(year)
    plt.show()


if __name__ == "__main__":
    main()
