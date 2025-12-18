"""
QUESTION:
# Task
 You're given a substring s of some cyclic string. What's the length of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?

# Example

 For` s = "cabca"`, the output should be `3`

 `"cabca"` is a substring of a cycle string "abcabcabcabc..." that can be obtained by concatenating `"abc"` to itself. Thus, the answer is 3.

# Input/Output


 - `[input]` string `s`

  Constraints: `3 ≤ s.length ≤ 15.`
  

 - `[output]` an integer
"""

def find_smallest_cyclic_length(s: str) -> int:
    """
    Finds the length of the smallest possible string that can be concatenated to itself many times
    to obtain a cyclic string containing the given substring `s`.

    Parameters:
    - s (str): The substring of the cyclic string.

    Returns:
    - int: The length of the smallest possible string.
    """
    return next((i for i in range(1, len(s)) if s.startswith(s[i:])), len(s))