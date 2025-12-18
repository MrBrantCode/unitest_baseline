"""
QUESTION:
This is a follow up from my kata The old switcheroo

Write
```python
def encode(str)
```
that takes in a string ```str``` and replaces all the letters with their respective positions in the English alphabet.

```python
encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'
```
String are case sensitive.
"""

def encode_alphabet_positions(input_str: str) -> str:
    """
    Encodes the input string by replacing each letter with its respective position in the English alphabet.
    Non-alphabetic characters remain unchanged.

    :param input_str: The input string to be encoded.
    :return: The encoded string.
    """
    return ''.join((str(ord(c.upper()) - 64) if c.isalpha() else c for c in input_str))