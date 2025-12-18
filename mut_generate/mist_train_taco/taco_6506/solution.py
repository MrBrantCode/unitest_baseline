"""
QUESTION:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 

## Examples

```python
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```
"""

def to_camel_case(text: str) -> str:
    """
    Converts dash/underscore delimited words into camel casing.

    The first word within the output retains its original capitalization,
    and subsequent words are capitalized.

    :param text: A string containing dash or underscore delimited words.
    :return: A string in camel case format.
    """
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])