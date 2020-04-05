from pandemic.data.WuhanVirus import CSSETimeSeries as cts


class Tools:

    def __init__(self, path):
        self.df = cts(path)

    def create_country_dropdown(self):
        dropdown = list()
        countries = self.df.get_country_list()
        for n in countries:
            dropdown.append({"label": n, "value": n})
        return dropdown

    def select_country(self, country):
        return self.select_countries(list(country))

    def select_countries(self, country_list):
        return self.df.merge(country_list).get_all_figures()
