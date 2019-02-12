
from abc import ABCMeta, abstractmethod
from cor_pattern.currency_type import CurrencyType


class BaseCurrencyHandler(metaclass=ABCMeta):
    """
    BaseCurrencyHandler exposes common methods and properties for other currency handlers

    """

    def __init__(self, next_currency_handler=None):
        self.next_currency_handler = next_currency_handler

    def convert(self, value, c_type):
        """
        Handles the common validation before hadling the conversion between currencies
        """
        if value is not None and isinstance(value, int):
            if c_type is not None and isinstance(c_type, CurrencyType):
                return self.handle_currency(value, c_type)
            else:
                return "Currency type cannot be none or not a valid currency type"
        return "The value cannot be none or non integer type"

    @abstractmethod
    def handle_currency(self, value, c_type):
        """
        Handles the currency converter request, based on a type and a value and a type
        of currency

        :param c_type: Has to be instance of CurrencyType Enum
        :param value: int valut to be converted to COP
        """
        pass

    @classmethod
    def handle_no_currency(cls, value, c_type):
        return "Cant convert value {} from currency of type {}. No handler available".format(value, c_type.name)


class UsDollarCurrencyHandler(BaseCurrencyHandler):
    base_proportion = 3115

    def handle_currency(self, value, c_type):
        if c_type == CurrencyType.USDollar:
            return self.base_proportion * value
        elif self.next_currency_handler is not None:
            return self.next_currency_handler.convert(value, c_type)
        return BaseCurrencyHandler.handle_no_currency(value, c_type)


class YenCurrencyHandler(BaseCurrencyHandler):
    base_proportion = 28.39

    def handle_currency(self, value, c_type):
        if c_type == CurrencyType.Yen:
            return self.base_proportion * value
        elif self.next_currency_handler is not None:
            return self.next_currency_handler.convert(value, c_type)
        return BaseCurrencyHandler.handle_no_currency(value, c_type)


class EurCurrencyHandler(BaseCurrencyHandler):
    base_proportion = 3539

    def handle_currency(self, value, c_type):
        if c_type == CurrencyType.Eur:
            return self.base_proportion * value
        elif self.next_currency_handler is not None:
            return self.next_currency_handler.convert(value, c_type)
        return BaseCurrencyHandler.handle_no_currency(value, c_type)
