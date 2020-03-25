import pandas as pd
import matplotlib.pyplot as plt
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
            return Countries(self.time_stamp, temp)
        else:
            return None


class Country:

    def __init__(self, country, time_stamp, time_series):
        self.country = country
        self.time_stamp = time_stamp
        self.t_data = self.transform(time_series)

    def transform(self, time_series):
        data_dict = {}
        for i in range(0, time_series.shape[0], 1):
            name = "/".join(time_series.iloc[i, 0:2].fillna(""))
            data_dict[name] = time_series.iloc[i, 4:].to_numpy()
        return data_dict

    def get_provence(self):
        return self.t_data.keys()

    def plot(self, xsize=15, ysize=10):
        fig, ax = plt.subplots(figsize=(xsize, ysize))
        for n, d in self.t_data.items():
            ax.plot_date(x=self.time_stamp.values, y=d, label=n, marker="o",
                         ls="-")
        ax.set_yscale("log")
        ax.set_ylim(1e0, 1e5)
        ax.set_ylabel("Cases Confirmed")
        ax.set_xlabel("Date")
        ax.set_title("Confirmed")
        ax.xaxis.set_tick_params(rotation=30, labelsize=10)
        ax.legend()

    def plot_state(self, state, xsize=15, ysize=10):
        data_state = self.t_data[state+"/"+self.country]
        fig, ax = plt.subplots(figsize=(xsize, ysize))
        ax.plot_date(x=self.time_stamp.values, y=data_state, label=state + "/" + self.country, marker="o", ls="-")
        ax.set_yscale("log")
        ax.set_ylim(1e0, 1e5)
        ax.set_ylabel("Cases Confirmed")
        ax.set_xlabel("Date")
        ax.xaxis.set_tick_params(rotation=30, labelsize=10)
        ax.legend()

class Countries:

    def __init__(self, time_stamp, time_series):
        self.time_stamp = time_stamp
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