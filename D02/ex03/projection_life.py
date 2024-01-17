from load_csv import load
import pandas as pd

def main():
    df_income = load("income_per_person_gdppercapita\
                     _ppp_inflation_adjusted.csv")
    df_life_expect = load("life_expectancy_years.csv")

if __name__ == "__main__":
    main()
