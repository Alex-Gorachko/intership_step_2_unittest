import unittest
from calculator import calculator

class CalculatorTest(unittest.TestCase):
    def test_normal1(self):
        res = calculator(1, 2, '+')
        self.assertEqual(res, 3)

    def test_normal2(self):
        res = calculator(3, 1, '-')
        self.assertEqual(res, 2)

    def test_normal3(self):
        res = calculator(10,  2, '/')
        self.assertEqual(res, 5)

    def test_normal4(self):
        res = calculator(8, 4, '*')
        self.assertEqual(res, 32)

    def test_normal5(self):
        res = calculator(5, 2, '**')
        self.assertEqual(res, 25)

if  __name__ == '__main__':
    unittest.main()
