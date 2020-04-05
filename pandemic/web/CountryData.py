from pandemic.viz.lplot import plot_figure_of, plot_all_figures


class CountryData:

    def __init__(self, df):
        self.df = df

    def get_provence(self):
        return self.df.columns

    def get_figure_of(self, province):
        return plot_figure_of(self.df, province)

    def get_all_figures(self):
        return plot_all_figures(self.df)
