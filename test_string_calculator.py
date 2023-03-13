import unittest
from stringCalculator import stringCalculator


class TestStringCalculator(unittest.TestCase):

    # Test task 1 and 2
    def test_calculate(self):
        calculator = stringCalculator()
        self.assertEqual(calculator.Calculate1(""), 0)
        self.assertEqual(calculator.Calculate1("5"), 5)
        self.assertEqual(calculator.Calculate1("-10"), -10)


    def test_calculate3(self):
        calculator3 = stringCalculator()
        self.assertEqual(calculator3.Calculate3("1,1"), 2)
        # self.assertEqual(calculator3.Calculate2("1", "1"), 0)
        self.assertEqual(calculator3.Calculate3("2,5"), 7)

    # Test task 4
    def test_calculate4(self):
        calculator4 = stringCalculator()
        self.assertEqual(calculator4.Calculate4("1\n6"), 7)

    # test task 5
    def test_calculate5(self):
        calculator5 = stringCalculator()
        self.assertEqual(calculator5.Ccalculate5("2\n3\n4"), 9)
        self.assertEqual(calculator5.Ccalculate5("2\n3\n4"), 9)

    # Test task 7
    def test_calculate7(self):
        calculator7 = stringCalculator()
        self.assertEqual(calculator7.Ccalculate7("2\n3\n1001"), 5)
        self.assertEqual(calculator7.Ccalculate7("2\n3\n1001"), 5)


if __name__ == '__main__':
    unittest.main()
