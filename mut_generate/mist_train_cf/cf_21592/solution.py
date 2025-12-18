"""
QUESTION:
Write a function named compare_strings that compares two input strings and returns 0 if they are identical, 1 if the first string is lexicographically greater than the second string, or -1 if the second string is lexicographically greater than the first string. The comparison should consider case-sensitivity and Unicode values of characters. The function should ignore any whitespace characters in the middle of the strings during comparison and handle any leading or trailing whitespace characters in the input strings. The function should also achieve a time complexity of O(n), where n is the length of the longer string.
"""

def compare_strings(a, b):
    # Trim leading and trailing whitespace characters
    a = a.strip()
    b = b.strip()

    # Initialize pointers
    pointer_a = 0
    pointer_b = 0

    # Iterate through the characters
    while pointer_a < len(a) and pointer_b < len(b):
        char_a = a[pointer_a]
        char_b = b[pointer_b]

        # Ignore whitespace characters
        if char_a.isspace():
            pointer_a += 1
            continue
        if char_b.isspace():
            pointer_b += 1
            continue

        # Compare characters
        if char_a != char_b:
            # Compare Unicode values
            if ord(char_a) > ord(char_b):
                return 1
            else:
                return -1

        # Move to the next character
        pointer_a += 1
        pointer_b += 1

    # Compare remaining characters if one string is longer
    if pointer_a < len(a):
        return 1
    elif pointer_b < len(b):
        return -1
    else:
        return 0