import unittest
import dash_core_components


class MyTestCase(unittest.TestCase):

    def test_dash_version(self):
        print(dash_core_components.__version__)


if __name__ == '__main__':
    unittest.main()
