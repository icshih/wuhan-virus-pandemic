import unittest
import dash_core_components
from pathlib import Path


class TestDash(unittest.TestCase):

    def test_dash_version(self):
        print(dash_core_components.__version__)

    def test_data_location(self):
        file = "../data/time_series_covid19_confirmed_global.csv"
        p = Path(file)
        print(p.exists())


if __name__ == '__main__':
    unittest.main()
