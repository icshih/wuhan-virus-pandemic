from pandemic.viz.lplot import plot_figure_of, plot_all_figures, plot_figure_country_region


class CountryData:

    def __init__(self, df):
        self.df = df

    def get_provence(self):
        return self.df.columns

    def pick_country_region(self, country_list):
        return self.df[country_list]

    def get_figure_country_region(self, country_list):
        return plot_figure_country_region(self.df[country_list])

    def get_figure_of(self, province):
        return plot_figure_of(self.df, province)

    def get_all_figures(self):
        return plot_all_figures(self.df)
