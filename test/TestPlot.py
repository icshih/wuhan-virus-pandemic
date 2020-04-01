import unittest

from pandemic.data.wuhanvirus import WuhanTimeSeries


class TestPlot(unittest.TestCase):
    path = "resources/time_series_covid19_confirmed_global_unit_test.csv"
    #path = "../data/time_series_covid19_confirmed_global.csv"
    wts = WuhanTimeSeries(path)

    def test_lplot_plot(self):
        test = self.wts.get_country("Afghanistan")
        test.p_engine = "plotly"
        test.plot()

    def test_lplot_plot_countries(self):
        countries = ["Afghanistan", "Albania", "Algeria", "Australia"]
        test = self.wts.get_countries(countries)
        test.p_engine = "plotly"
        test.plot()

    def test_mplot_plot(self):
        test = self.wts.get_country("Australia")
        test.plot("New South Wales")

    def test_lplot_plots(self):
        test = self.wts.get_country("Australia")
        test.p_engine = "plotly"
        test.plots()

    def test_mplot_plots(self):
        test = self.wts.get_country("Australia")
        test.plots()


if __name__ == '__main__':
    unittest.main()
