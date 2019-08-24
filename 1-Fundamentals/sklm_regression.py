#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sklearn.linear_model as sklm


def load_data(oecd='', gdp=''):
    if not (oecd and gdp):
        oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
        gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")
        return oecd_bli, gdp_per_capita
    else:
        return None


def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]


def prep_data(oecd='', gdp=''):
    # prepare
    oecd, gdp = load_data(oecd='', gdp='')
    country_stats = prepare_country_stats(oecd, gdp)
    X = np.c_[country_stats["GDP per capita"]]
    y = np.c_[country_stats["Life satisfaction"]]
    return X, y, country_stats

def train_run_sklm(oecd='', gdp=''):
    X, y, country_stats = prep_data(oecd='', gdp='')

    # plot
    country_stats.plot(kind='scatter', x="GDP per capita", y="Life satisfaction")
    plt.show()

    # init linear model
    model = sklm.LinearRegression()
    
    # train
    model.fit(X, y)

    # predict for Cyprus GDP=22587
    print(model.predict([[22587]]))


if __name__=="__main__":
    try:
        train_run_sklm(sys.argv[1], sys.argv[2])
    except:
        print("\nNo input file given, get them from these links:")
        print("Better Life Index: https://stats.oecd.org/index.aspx?DataSetCode=BLI")
        print("GDP Per Capita: https://www.imf.org/external/datamapper/NGDPDPC@WEO/OEMDC/ADVEC/WEOWORLD")
        print("Clean and convert them into csv")
    

