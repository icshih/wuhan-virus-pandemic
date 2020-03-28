import unittest
import pandas as pd

from pandemic.data.wuhanvirus import WuhanTimeSeries


class MyTestCase(unittest.TestCase):

    path = "resources/time_series_covid19_confirmed_global_unit_test.csv"
    data = pd.read_csv(path)
    wts = WuhanTimeSeries(path)

    def test_country_get_province(self):
        af = self.data.head(1)
        self.assertEqual(True, af["Province/State"].isnull().values.any())
        au = self.data.iloc[12]
        self.assertEqual("South Australia", au["Province/State"])

    def test_set_time_stamp(self):
        days = self.data.iloc[0, 4:].size
        ts = pd.date_range('1/22/2020', periods=days)
        self.assertCountEqual(ts, self.wts.time_stamp)
        time_series = self.wts.get_time_series_all().iloc[0, 4:]
        self.assertEqual(ts.size, time_series.values.size)

    def test_get_country_list(self):
        test = list()
        countries = self.wts.get_country_list()
        for n in countries:
            test.append({"label": n, "value":n})
        for t in test:
            print(t["label"] + " = " + t["value"])

    def test_transform(self):
        test = self.wts.get_time_series_of("Afghanistan")
        data_dict = {}
        for i in range(0, test.shape[0], 1):
            name = "/".join(test.iloc[i, 0:2].fillna(""))
            data_dict[name] = test.iloc[i, 4:].to_numpy()
        print(data_dict)

    def test_get_country(self):
        af = self.wts.get_country("Afghanistan")


if __name__ == '__main__':
    unittest.main()
