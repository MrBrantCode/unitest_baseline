"""
QUESTION:
Your goal is to create a function to format a number given a template; if the number is not present, use the digits `1234567890` to fill in the spaces.

A few rules:

* the template might consist of other numbers, special characters or the like: you need to replace only alphabetical characters (both lower- and uppercase);
* if the given or default string representing the number is shorter than the template, just repeat it to fill all the spaces.

A few examples:

```python
numeric_formatter("xxx xxxxx xx","5465253289") == "546 52532 89"
numeric_formatter("xxx xxxxx xx") == "123 45678 90"
numeric_formatter("+555 aaaa bbbb", "18031978") == "+555 1803 1978"
numeric_formatter("+555 aaaa bbbb") == "+555 1234 5678"
numeric_formatter("xxxx yyyy zzzz") == "1234 5678 9012"
```
"""

from itertools import cycle

def format_number_with_template(template: str, number: str = '1234567890') -> str:
    """
    Formats a number according to a given template. If the number is not provided,
    it uses the digits '1234567890' to fill in the spaces.

    :param template: The template string containing placeholders for numbers.
    :param number: The string representing the number to fill in the template.
                   Defaults to '1234567890'.
    :return: The formatted string with numbers filled in according to the template.
    """
    number_cycle = cycle(number)
    return ''.join((next(number_cycle) if c.isalpha() else c for c in template))