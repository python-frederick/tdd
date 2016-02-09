import operator


class CalculatorError(Exception):
    pass


class Calculator(object):

    def add(self, *args):
        try:
            return reduce(operator.add, args)
        except TypeError:
            raise CalculatorError('Sorry! Your input is invalid.')
