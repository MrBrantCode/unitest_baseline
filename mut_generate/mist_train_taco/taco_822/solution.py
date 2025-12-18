"""
QUESTION:
You have to create a function that converts integer given as string into ASCII uppercase letters.

All ASCII characters have their numerical order in table. 

For example,

```
from ASCII table, character of number 65 is "A".
```

Numbers will be next to each other, So you have to split given number to two digit long integers.

For example, 

```
'658776' to [65, 87, 76] and then turn it into 'AWL'.
```
"""

def convert_number_to_ascii_uppercase(number: str) -> str:
    """
    Converts a given string of numbers into ASCII uppercase letters.

    Parameters:
    number (str): A string of digits to be converted.

    Returns:
    str: A string of ASCII uppercase letters corresponding to the given number.
    """
    return ''.join((chr(int(number[a:a + 2])) for a in range(0, len(number), 2)))