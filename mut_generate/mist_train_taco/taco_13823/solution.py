"""
QUESTION:
This kata is part of the collection [Mary's Puzzle Books](https://www.codewars.com/collections/marys-puzzle-books).

# Zero Terminated Sum

Mary has another puzzle book, and it's up to you to help her out! This book is filled with zero-terminated substrings, and you have to find the substring with the largest sum of its digits. For example, one puzzle looks like this:
```
"72102450111111090"
```
Here, there are 4 different substrings: `721`, `245`, `111111`, and `9`. The sums of their digits are `10`, `11`, `6`, and `9` respectively. Therefore, the substring with the largest sum of its digits is `245`, and its sum is `11`.

Write a function `largest_sum` which takes a string and returns the maximum of the sums of the substrings. In the example above, your function should return `11`.

### Notes:

- A substring can have length 0. For example, `123004560` has three substrings, and the middle one has length 0.
- All inputs will be valid strings of digits, and the last digit will always be `0`.
"""

def largest_sum(s: str) -> int:
    """
    Finds the maximum sum of the digits of any zero-terminated substring in the input string.

    Args:
        s (str): A string of digits where the last digit is always '0'.

    Returns:
        int: The maximum sum of the digits of any zero-terminated substring.
    """
    return max((sum(map(int, x)) for x in s.split('0')))