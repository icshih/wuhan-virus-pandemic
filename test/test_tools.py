import unittest


class MyTestCase(unittest.TestCase):
    def test_remove_symbol(self):
        taiwan = "Taiwan*"
        self.assertTrue(taiwan.__contains__("*"))
        tai = taiwan.replace("*", "")
        self.assertEqual(tai, "Taiwan")


if __name__ == '__main__':
    unittest.main()
