from pandemic.data.wuhanvirus import WuhanTimeSeries as wts


class Tools:

    def __init__(self, path):
        self.wvts = wts(path)

    def create_country_dropdown(self):
        dropdown = list()
        countries = self.wvts.get_country_list()
        for n in countries:
            if n.__contains__("*"):
                label = n.replace("*", "")
            else:
                label = n
            dropdown.append({"label": label, "value": n})
        return dropdown

    def select_country(self, country):
        return self.wvts.get_country(country).get_figure()

    def select_countries(self, country_list):
        return self.wvts.get_countries(country_list).get_figure()
