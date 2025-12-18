"""
QUESTION:
# Task
 You are given a string `s`. Every letter in `s` appears once. 
 
 Consider all strings formed by rearranging the letters in `s`. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length `n`, define its middle term to be the `(n/2)`th term.)

# Example

 For `s = "abc"`, the result should be `"bac"`.
```
The permutations in order are:
"abc", "acb", "bac", "bca", "cab", "cba"
So, The middle term is "bac".```

# Input/Output


 - `[input]` string `s`

  unique letters (`2 <= length <= 26`)

 - `[output]` a string

  middle permutation.
"""

def get_middle_permutation(s: str) -> str:
    """
    Returns the middle permutation of the input string `s` when all permutations are ordered lexicographically.

    Parameters:
    - s (str): A string containing unique letters. The length of the string is between 2 and 26.

    Returns:
    - str: The middle permutation of the input string.
    """
    sorted_s = sorted(s)
    if len(sorted_s) % 2 == 0:
        middle_index = len(sorted_s) // 2 - 1
        middle_char = sorted_s.pop(middle_index)
        return middle_char + ''.join(sorted_s[::-1])
    else:
        middle_index = len(sorted_s) // 2
        middle_char = sorted_s.pop(middle_index)
        return middle_char + get_middle_permutation(''.join(sorted_s))