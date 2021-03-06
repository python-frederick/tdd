import unittest

from calculator import Calculator, CalculatorError


class TestCalculator(unittest.TestCase):

    def test_adds_numbers(self):
        # Arrange
        calculator = Calculator()

        # Act
        result = calculator.add(1, 2)

        # Assert
        self.assertEqual(3, result)

    def test_adds_others(self):
        # Arrange
        calculator = Calculator()

        # Act/Assert
        self.assertRaises(CalculatorError, calculator.add, 1, 'gotcha!')

    def test_adds_many_numbers(self):
        # Arrange
        calculator = Calculator()

        # Act
        result = calculator.add(1, 2, 3)

        # Assert
        self.assertEqual(6, result)

    def test_adds_no_numbers(self):
        # Arrange
        calculator = Calculator()

        # Act
        result = calculator.add()

        # Assert
        self.assertEqual(0, result)
