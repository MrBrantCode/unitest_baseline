"""
QUESTION:
**This Kata is intended as a small challenge for my students**

All Star Code Challenge #16

Create a function called noRepeat() that takes a string argument and returns a single letter string of the **first** not repeated character in the entire string.

``` haskell
noRepeat "aabbccdde" `shouldBe` 'e'
noRepeat "wxyz"      `shouldBe` 'w'
noRepeat "testing"   `shouldBe` 'e'
```

Note:
ONLY letters from the english alphabet will be used as input
There will ALWAYS be at least one non-repeating letter in the input string
"""

def find_first_non_repeating_char(input_string: str) -> str:
    """
    Finds and returns the first non-repeating character in the input string.

    Args:
        input_string (str): A string containing only English alphabet letters.

    Returns:
        str: A single character string representing the first non-repeating character.
    """
    return next((c for c in input_string if input_string.count(c) == 1))