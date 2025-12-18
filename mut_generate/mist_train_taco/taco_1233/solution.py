"""
QUESTION:
Check if it is a vowel(a, e, i, o, u,) on the ```n``` position in a string (the first argument). Don't forget about uppercase.

A few cases:

```
{
checkVowel('cat', 1)  ->   true // 'a' is a vowel
checkVowel('cat', 0)  ->   false // 'c' is not a vowel
checkVowel('cat', 4)  ->   false // this position doesn't exist
}
```
P.S. If n < 0, return false
"""

def is_vowel_at_position(s: str, n: int) -> bool:
    """
    Check if the character at position `n` in the string `s` is a vowel.

    Parameters:
    - s (str): The input string.
    - n (int): The position in the string to check.

    Returns:
    - bool: True if the character at position `n` is a vowel, False otherwise.
    """
    return 0 <= n < len(s) and s[n].lower() in 'aeiou'