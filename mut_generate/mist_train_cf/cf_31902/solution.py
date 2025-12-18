"""
QUESTION:
Create a function `calculate_metrics` that takes a dictionary `a` as input and returns a dictionary containing the calculated financial metrics. The input dictionary `a` contains financial data with keys `'fifty_two_week_high'`, `'price_earnings_ratio'`, `'C'`, and `'P'`. The function should calculate the following metrics: 

- `H52`: The fifty-two week high, rounded to the nearest integer. If the data is not a valid number, it should be represented as `'_'`.
- `PE`: The price-earnings ratio, rounded to one decimal place. If the data is not a valid number, it should be represented as `'_'`.
- `Cp`: The percentage change, calculated as the integer result of rounding the ratio of `C` to `P` multiplied by 100. If there are any errors in the calculation, it should be represented as `'_'`.

The function should handle potential errors in the input data gracefully, ensuring that the calculated metrics are either valid numbers or represented as `'_'` in case of errors.
"""

def calculate_metrics(a: dict) -> dict:
    result = {}
    
    try:
        result['H52'] = int(round(float(a['fifty_two_week_high']), 0))
    except (ValueError, KeyError):
        result['H52'] = '_'
    
    try:
        result['PE'] = round(float(a['price_earnings_ratio']), 1)
    except (ValueError, KeyError):
        result['PE'] = '_'
    
    try:
        result['Cp'] = int(round(float(a['C']) / float(a['P']) * 100))
    except (ValueError, KeyError, ZeroDivisionError):
        result['Cp'] = '_'
    
    return result