"""
QUESTION:
Create a function called `currency_formatter` that takes a list of decimal numbers and a currency code (USD, EUR, or GBP) as input and returns a dictionary where the keys are the decimal numbers and the values are the corresponding currency formatted strings. The function should handle large numbers and very small numbers, and it should not perform actual currency conversion, only format the decimal numbers as if they were in the specified currency.
"""

import locale

def currency_formatter(decimal_list, currency):
    results = {}
    for decimal_number in decimal_list:
        if currency == 'USD':
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        elif currency == 'EUR':
            locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
        elif currency == 'GBP':
            locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
        else:
            return "The provided currency option is not supported."
        currency_str = locale.currency(decimal_number, grouping=True)
        results[decimal_number] = currency_str
    return results