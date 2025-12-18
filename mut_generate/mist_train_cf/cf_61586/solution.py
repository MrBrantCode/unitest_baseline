"""
QUESTION:
Write a function called `can_form_palindrome` that checks if a given string can be rearranged to form a palindrome. The function should ignore special characters, spaces, and case sensitivity, and return a tuple containing a boolean value indicating whether the string can be rearranged into a palindrome, a message explaining the result, and the palindrome itself if one exists. The function should work correctly for strings of any length.
"""

def can_form_palindrome(s):
    # Remove special characters and spaces, convert to lower case
    cleaned_str = ''.join(e for e in s if e.isalnum()).lower()

    # Count the frequency of each character 
    freq = {}
    for char in cleaned_str:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1

    # Check if more than one character has an odd count. 
    # In a palindrome, at most one character can have an odd count.
    odd_count = 0
    for count in freq.values():
        odd_count += count % 2

    if odd_count > 1:
        return False, 'Input cannot be rearranged to form a palindrome.', ''
    else:
        # Build the palindrome
        first_half = ''.join(k * (v // 2) for k, v in freq.items())
        second_half = first_half[::-1]
        middle = ''.join(k for k, v in freq.items() if v % 2)
        palindrome = first_half + middle + second_half
        return True, 'Input can be rearranged to form a palindrome.', palindrome