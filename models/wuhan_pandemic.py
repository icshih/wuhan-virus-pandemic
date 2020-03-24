import pandas as pd
import matplotlib.pyplot as plt
import logging


class WuhanTimeSeries:

    def __init__(self, path_to_time_series):
        self.data_time_series = pd.read_csv(path_to_time_series)

    def get_country_list(self):
        return self.data_time_series["Country/Region"]

    def get_time_series(self):
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
            return Country(temp)
        else:
            return None

    def get_countries(self, country_list):
        temp = self.data_time_series[self.data_time_series["Country/Region"].isin(country_list)]
        if temp is not None:
            return Countries(temp)
        else:
            return None


class Country:

    def __init__(self, time_series):
        self.time_series = time_series

    def plot(self):
        fig, axs = plt.subplots(figsize=(10, 10));
        self.time_series.iloc[0, 4:].plot.line(ax=axs)
        axs.set_yscale("log")
        axs.set_ylim(1e0, 1e5)
        axs.set_ylabel("Cases Confirmed")
        axs.set_xlabel("Date")
        plt.plot()


class Countries:

    def __init__(self, time_series):
        self.time_series = time_series

    def plot(self):
        fig, axs = plt.subplots(figsize=(10, 10));
        for i in range(0, self.time_series.shape[0], 1):
            self.time_series.iloc[i, 4:].plot.line(ax=axs)
        axs.set_yscale("log")
        axs.set_ylim(1e0, 1e5)
        axs.set_ylabel("Cases Confirmed")
        axs.set_xlabel("Date")
        plt.plot()