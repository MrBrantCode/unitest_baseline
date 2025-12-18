"""
QUESTION:
Write a function `compare_strings(a, b)` that compares two strings lexicographically, ignoring whitespace characters and considering case-sensitivity and Unicode values. Return 0 if the strings are identical, 1 if `a` is greater than `b`, and -1 if `b` is greater than `a`. The function should have a time complexity of O(n), where n is the length of the longer string, and a constant space complexity of O(1).
"""

def compare_strings(a, b):
    # Remove leading and trailing whitespace characters
    a = a.strip()
    b = b.strip()

    # Get the lengths of the strings
    len_a = len(a)
    len_b = len(b)

    # Compare each character of the strings
    i = 0
    j = 0
    while i < len_a and j < len_b:
        # Ignore whitespace characters in the middle of the strings
        if a[i].isspace():
            i += 1
            continue
        if b[j].isspace():
            j += 1
            continue

        # Compare characters based on their Unicode values
        if ord(a[i]) > ord(b[j]):
            return 1
        elif ord(a[i]) < ord(b[j]):
            return -1

        # Move to the next characters
        i += 1
        j += 1

    # Compare the remaining characters
    if i < len_a:
        return 1
    elif j < len_b:
        return -1
    else:
        return 0