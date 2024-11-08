import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add method
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Test cases for subtract method
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # Test cases for multiply method
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # Test cases for divide method
    def test_divide_exact_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_non_exact_division(self):
        self.assertEqual(self.calc.divide(7, 3), 2)

    # Test cases for modulo method
    def test_modulo_exact_division(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

    def test_modulo_non_exact_division(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()