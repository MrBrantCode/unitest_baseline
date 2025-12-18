"""
QUESTION:
Write a function `longest_substring` that finds the length of the longest substring without repeating characters in a given string that meets the following conditions:
- contains at least one uppercase letter, one lowercase letter, and one digit
- is in lexicographical order
- starts with an uppercase letter
- does not contain any special characters or symbols.
"""

def longest_substring(s: str) -> int:
    """
    This function finds the length of the longest substring without repeating characters 
    in a given string that meets the conditions:
    - contains at least one uppercase letter, one lowercase letter, and one digit
    - is in lexicographical order
    - starts with an uppercase letter
    - does not contain any special characters or symbols.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring that meets the conditions.
    """

    def is_valid(c):
        """Check if a character is an uppercase letter, lowercase letter, or digit."""
        return c.isupper() or c.islower() or c.isdigit()

    def has_upper_lower_digit(s):
        """Check if a string contains at least one uppercase letter, one lowercase letter, and one digit."""
        return any(c.isupper() for c in s) and any(c.islower() for c in s) and any(c.isdigit() for c in s)

    def is_lexicographical_order(s):
        """Check if a string is in lexicographical order."""
        return s == ''.join(sorted(s))

    start = 0
    max_length = 0
    char_set = set()

    for end, c in enumerate(s):
        # If the character is not valid, reset the window
        if not is_valid(c):
            start = end + 1
            char_set = set()
        # If the character is already in the set, reset the window
        elif c in char_set:
            while c in char_set:
                char_set.remove(s[start])
                start += 1
        else:
            char_set.add(c)
            # Check if the current substring meets all conditions
            if (end - start + 1) > max_length and start == 0 and is_lexicographical_order(s[start:end + 1]) and has_upper_lower_digit(s[start:end + 1]):
                max_length = end - start + 1

    return max_length