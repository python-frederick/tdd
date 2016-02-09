class CalculatorError(Exception):
    pass


class Calculator(object):

    def add(self, *args):
        try:
            return sum(args)
        except TypeError as ex:
            raise CalculatorError('Sorry! Your input is invalid.') from ex
