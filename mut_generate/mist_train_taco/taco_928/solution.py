"""
QUESTION:
In this Kata, you will be given a string and your task is to determine if that string can be a palindrome if we rotate one or more characters to the left.

```Haskell
solve("4455") = true, because after 1 rotation, we get "5445" which is a palindrome
solve("zazcbaabc") = true, because after 3 rotations, we get "abczazcba", a palindrome
```

More examples in test cases. Input will be strings of lowercase letters or numbers only.

Good luck!
"""

def can_form_palindrome_by_rotation(s: str) -> bool:
    """
    Determines if the given string can be a palindrome by rotating one or more characters to the left.

    Args:
        s (str): The input string of lowercase letters or numbers.

    Returns:
        bool: True if the string can be a palindrome by rotation, False otherwise.
    """
    return any((s[i + 1:] + s[:i + 1] == s[i::-1] + s[:i:-1] for i in range(len(s))))