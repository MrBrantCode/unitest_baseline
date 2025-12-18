"""
QUESTION:
Your task is to convert a given number into a string with commas added for easier readability.  The number should be rounded to 3 decimal places and the commas should be added at intervals of three digits before the decimal point. There does not need to be a comma at the end of the number.

You will receive both positive and negative numbers.

## Examples

```python
commas(1) == "1"
commas(1000) == "1,000"
commas(100.2346) == "100.235"
commas(1000000000.23) == "1,000,000,000.23"
commas(-1) == "-1"
commas(-1000000.123) == "-1,000,000.123"
```
"""

def format_number_with_commas(num):
    """
    Formats a given number with commas for easier readability and rounds it to 3 decimal places.

    Parameters:
    num (float or int): The number to be formatted.

    Returns:
    str: The formatted number as a string with commas and rounded to 3 decimal places.
    """
    formatted_num = '{:,.3f}'.format(num)
    return formatted_num.rstrip('0').rstrip('.')