import pandas as pd
import matplotlib.pyplot as plt
from pandemic.viz import mplot
from pandemic.viz import lplot
import logging


class WuhanTimeSeries:

    def __init__(self, path_to_time_series):
        self.data_time_series = pd.read_csv(path_to_time_series)
        self.time_stamp = self.set_time_stamp()

    def set_time_stamp(self):
        days = self.data_time_series.iloc[0, 4:].size
        return pd.date_range('1/22/2020', periods=days)

    def get_country_list(self):
        return self.data_time_series["Country/Region"].unique()

    def get_time_series_all(self):
        return self.data_time_series

    def get_time_series_of(self, country):
        temp = self.data_time_series[self.data_time_series["Country/Region"] == country]
        if temp.shape[0] != 0:
            return temp
        else:
            logging.error("No data for " + country)
            return None

    def get_country(self, country):
        temp = self.get_time_series_of(country)
        if temp is not None:
            return Country(country, self.time_stamp, temp)
        else:
            return None

    def get_countries(self, country_list):
        temp = self.data_time_series[self.data_time_series["Country/Region"].isin(country_list)]
        if temp is not None:
            return Countries(country_list, self.time_stamp, temp)
        else:
            return None


def transform(time_series):
    data_dict = {}
    for i in range(0, time_series.shape[0], 1):
        name = "/".join(time_series.iloc[i, 0:2].fillna(""))
        data_dict[name] = time_series.iloc[i, 4:].to_numpy()
    return data_dict


class Country:

    def __init__(self, country, time_stamp, time_series):
        self.country = country
        self.time_stamp = time_stamp
        self.t_data = transform(time_series)
        self.p_engine = "matplotlib"

    def get_provence(self):
        return self.t_data.keys()

    def get_figure_of(self, province=""):
        return lplot.plot_country_state(self.country, self.time_stamp, self.t_data, province)

    def get_figure(self):
        return lplot.plots(self.time_stamp, self.t_data)

    def plot(self, province="", xsize=15, ysize=10):
        if self.p_engine == "plotly":
            self.get_figure_of(province).show()
        else:
            mplot.plot_country_state(self.country, self.time_stamp, self.t_data, province, xsize, ysize)

    def plots(self, xsize=15, ysize=10):
        if self.p_engine == "plotly":
            self.get_figure().show()
        else:
            mplot.plots(self.time_stamp, self.t_data, xsize, ysize)


class Countries:

    def __init__(self, country_list, time_stamp, time_series):
        self.country_list = country_list
        self.time_stamp = time_stamp
        self.t_data = transform(time_series)

    def plot(self, xsize=15, ysize=10):
        fig, ax = plt.subplots(figsize=(xsize, ysize))
        for c in self.country_list:
            ax.plot_date(x=self.time_stamp.values, y=self.t_data["/"+c], label=c, marker="o", ls="-")
        ax.set_yscale("log")
        ax.set_ylim(1e0, 1e5)
        ax.set_ylabel("Cases Confirmed")
        ax.set_xlabel("Date")
        ax.set_title("Confirmed")
        ax.xaxis.set_tick_params(rotation=30, labelsize=10)
        ax.legend()