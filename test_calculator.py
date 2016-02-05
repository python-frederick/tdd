import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_adds_numbers(self):
        # Arrange
        calculator = Calculator()

        # Act
        result = calculator.add(1, 2)

        # Assert
        self.assertEqual(3, result)
