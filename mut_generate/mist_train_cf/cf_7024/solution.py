"""
QUESTION:
Implement a function `compare_strings(a, b)` that compares two strings lexicographically. The function should return 0 if the strings are identical, 1 if string `a` is lexicographically greater than `b`, or -1 if string `b` is lexicographically greater than `a`. The comparison should be case-sensitive and based on the Unicode values of the characters. The function should ignore any leading or trailing whitespace characters and any whitespace characters in the middle of the strings. The time complexity should be O(n), where n is the length of the longer string, and the space complexity should be O(1), with no extra data structures that grow with the size of the input strings.
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