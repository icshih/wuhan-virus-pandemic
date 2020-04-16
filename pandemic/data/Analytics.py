import pandas as pd
import numpy as np
from scipy.optimize import curve_fit


def fit(df_country, date, period=7):
    t_s = pd.Timestamp(date)
    t_b = t_s - pd.Timedelta(period, unit="days")
    y = np.log10(df_country[t_b:t_s])
    x = range(len(y))
    popt, pcov = curve_fit(func, x, y)
    return df_country[t_b:t_s].index, popt, pcov


def func(x, a, b):
    return a * np.exp(b * x)