class CalculatorError(Exception):
    pass


class Calculator(object):

    def add(self, x, y):
        try:
            return x + y
        except TypeError:
            raise CalculatorError('Sorry! Your input is invalid.')
