import pandas as pd
from pandemic.web.CountryData import CountryData


def optimise(path_csv):
    """
    Fill the value of Province/State
    Remove the * symbol after the name of Country/Region
    :return:
    """
    df = pd.read_csv(path_csv)
    for index, row in df.iterrows():
        country = row["Country/Region"]
        if country.__contains__("*"):    # Remove * symbol after country's name
            country = country.replace("*", "")
            df.iloc[index, 1] = country
        if pd.isna(row["Province/State"]):    # if the column is NaN, fill the value of the Country/Region
            df.iloc[index, 0] = country
    return df


class CSSETimeSeries:

    def __init__(self, path_to_time_series):
        self.ts = optimise(path_to_time_series)

    def get_country_data(self, country):
        """
        Get the CSSE data of the country.
        The Lat and Long columns are removed and table is pivoted so the data column is the index.
        :param country:
        :return: a CountryData object
        """
        temp = self.ts[self.ts["Country/Region"] == country]
        if temp.shape[0] == 0:
            print(country + " is not in the dataset.")
            data = None
        else:
            data = temp.drop(columns=["Lat", "Long"]).pivot_table(columns="Province/State")
            data.index = pd.to_datetime(data.index)
        return CountryData(data.sort_index())

    def select(self, country_list):
        """
        Select the CSSE data from a list of countries.
        :param country_list:
        :return: a directory of CountryData objects
        """
        countries = dict()
        for c in country_list:
            tmp = self.get_country_data(c)
            if tmp is not None:
                countries[c] = tmp
        return countries

    def merge(self, country_list):
        """
        Merge the CountryData from a list of countries
        Only the columns whose name of Province/State equals to that of the country are merged.
        :param country_list:
        :return: a CountryData object
        """
        countries = self.select(country_list)
        data = list()
        for k in countries.keys():
            data.append(countries.get(k).df[k])
        return CountryData(pd.concat(data, axis=1))

    def get_country_list(self):
        return self.ts["Country/Region"].unique()


