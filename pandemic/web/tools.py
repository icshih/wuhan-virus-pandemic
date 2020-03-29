from pandemic.data.wuhanvirus import WuhanTimeSeries as wts


class Tools:

    def __init__(self, path):
        self.wvts = wts(path)

    def create_country_dropdown(self):
        dropdown = list()
        countries = self.wvts.get_country_list()
        for n in countries:
            dropdown.append({"label": n, "value": n})
        return dropdown

    def select_country(self, country):
        return self.wvts.get_country(country).get_figure()