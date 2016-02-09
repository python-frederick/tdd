import functools
import operator


class CalculatorError(Exception):
    pass


class Calculator(object):

    def add(self, *args):
        try:
            return functools.reduce(operator.add, args, 0)
        except TypeError as ex:
            raise CalculatorError('Sorry! Your input is invalid.') from ex
