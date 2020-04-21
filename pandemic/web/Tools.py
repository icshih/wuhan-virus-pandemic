from pandemic.data.WuhanVirus import CSSETimeSeries as cts
from pandemic.viz.lplot import plot_confirmed_death_recovered_by, plot_confirmed_infection_rate
import pandas as pd


class Tools:

    def __init__(self, path_confirmed, path_death, path_recovered):
        self.path_confirmed = path_confirmed
        self.path_death = path_death
        self.path_recovered = path_recovered
        self.confirmed, self.death, self.recovered = self._load()

    def _load(self):
        confirmed = cts(self.path_confirmed).get_grouped_country_data()
        death = cts(self.path_death).get_grouped_country_data()
        recovered = cts(self.path_recovered).get_grouped_country_data()
        return confirmed, death, recovered

    def _show_confirmed_only(self, country_list):
        return self.confirmed.get_figure_country_region(country_list)

    def _show_confirmed_death_recovered(self, country):
        df = pd.concat([self.confirmed.df[country], self.death.df[country], self.recovered.df[country]], axis=1)
        df.columns = ["Confirmed", "Death", "Recovered"]
        return plot_confirmed_death_recovered_by(df)

    def _show_confirmed_death_recovered_infection_rate(self, country, date=None, period=7):
        df = pd.concat([self.confirmed.df[country], self.death.df[country], self.recovered.df[country]], axis=1)
        df.columns = ["Confirmed", "Death", "Recovered"]
        # if date is not None:
        #     return plot_confirmed_infection_rate(df, date, period=period)
        # else:
        return plot_confirmed_infection_rate(df, date, period)

    def create_country_dropdown(self):
        """
        Create Country dropdown manu.
        :return:
        """
        dropdown = list()
        countries = self.confirmed.df.columns
        for n in countries:
            dropdown.append({"label": n, "value": n})
        return dropdown

    def select_country(self, country):
        return self.select_countries(list(country))

    def select_countries(self, country_list, date=None):
        """
        Display COVID-19 epidemics in the selected country.
        :param country_list: One or more countries. If the list length is 1, full COVID-19 data is plotted,
                             otherwise, the confirmed cases of the selected countries are plotted.
        :param date: (Optional) Examination of the infection rate in the duration of 7 days (default value)
                     up to the date.
        :return:
        """
        if len(country_list) == 1:
            return self._show_confirmed_death_recovered_infection_rate(country_list[0], date=date)
        else:
            return self._show_confirmed_only(country_list)

    def reload(self):
        """
        Reload the csv files
        :return:
        """
        self.confirmed, self.death, self.recovered = self.load()
