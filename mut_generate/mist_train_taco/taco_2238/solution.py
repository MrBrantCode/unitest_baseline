"""
QUESTION:
Create a function `longer` that accepts a string and sorts the words in it based on their respective lengths in an ascending order. If there are two words of the same lengths, sort them alphabetically. Look at the examples below for more details.

```python
longer("Another Green World") => Green World Another
longer("Darkness on the edge of Town") => of on the Town edge Darkness
longer("Have you ever Seen the Rain") => the you Have Rain Seen ever
```

Assume that only only Alphabets will be entered as the input.
Uppercase characters have priority over lowercase characters. That is,
```python
longer("hello Hello") => Hello hello
```

Don't forget to rate this kata and leave your feedback!! 
Thanks
"""

def sort_words_by_length(s: str) -> str:
    """
    Sorts the words in the input string based on their lengths in ascending order.
    If two words have the same length, they are sorted alphabetically with uppercase
    characters having priority over lowercase characters.

    Parameters:
    s (str): The input string containing words to be sorted.

    Returns:
    str: A string where the words are sorted based on their lengths and alphabetical order.
    """
    return ' '.join(sorted(s.split(), key=lambda w: (len(w), w)))