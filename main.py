from cor_pattern.currencies import UsDollarCurrencyHandler, EurCurrencyHandler, YenCurrencyHandler
from cor_pattern.currency_type import CurrencyType
from math import floor

def main():

    usdollar_handler = UsDollarCurrencyHandler()
    eur_handler = EurCurrencyHandler(usdollar_handler)
    yen_handler = YenCurrencyHandler(eur_handler)

    (value, currency_type_choice) = get_user_input()


    result = yen_handler.convert(value, currency_type_choice)

    if isinstance(result, int):
        result = floor(result)
        print("{} {} is equal to {} COP".format(value, currency_type_choice.name, result))
    else:
        print(result)


def get_user_input():
    print("Currency converter 1.0")
    print("Please select the currency you cant to convert to COP")

    for currency_type in CurrencyType:
        print("{}: {}".format(currency_type.value, currency_type.name))
    currency_type_choice = int(input())

    currency_type_choice = get_currency_from_list(currency_type_choice)

    value = input("Enter the value you want to convert: ")

    try:
        value = int(value)
    except ValueError:
        print("cant convert to int")
        return (None, None)


    return (value, currency_type_choice)


def get_currency_from_list(index):
    c_list = list(CurrencyType)

    return c_list[index - 1]

if __name__ == "__main__":
    main()
