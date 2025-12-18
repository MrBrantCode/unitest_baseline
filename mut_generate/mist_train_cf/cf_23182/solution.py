"""
QUESTION:
Create a function `format_number` that takes a float `number`, a positive integer `decimal_places`, and a boolean `truncate` as input. The function should format the `number` to have exactly `decimal_places` decimal places. If `truncate` is `False`, the function should round the `number`. If `truncate` is `True`, the function should truncate the `number` without rounding.
"""

def format_number(n, decimal_places, truncate):
    if truncate:
        return float("{:.{dp}f}".format(n, dp=decimal_places))
    else:
        return round(n, decimal_places)