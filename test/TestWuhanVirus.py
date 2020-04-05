import unittest
from pandemic.data.WuhanVirus import CSSETimeSeries


class TestWuhanVirus(unittest.TestCase):

    path = "resources/time_series_covid19_confirmed_global_unit_test.csv"
    wts = CSSETimeSeries(path)

    def test_get_country_list(self):
        print(self.wts.get_country_list())

    def test_get_country_data(self):
        af = self.wts.get_country_data("Afghanistan")
        print(af.df)

    def test_select(self):
        test = self.wts.select(["Argentina", "Afghanistan"])
        print(test)

    def test_merge(self):
        test = self.wts.merge(["Argentina", "Afghanistan"])
        print(test)


if __name__ == '__main__':
    unittest.main()
