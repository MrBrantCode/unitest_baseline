"""
QUESTION:
Find the length of the longest substring without repeating characters that contains at least one uppercase letter, one lowercase letter, and one digit, and is in lexicographical order.

The function should be named `length_of_longest_substring` and take a string as input. The function should return the length of the longest substring that meets the specified conditions.
"""

def length_of_longest_substring(string):
    start = 0
    end = 0
    maxLen = 0
    upper = False
    lower = False
    digit = False
    charSet = set()

    while end < len(string):
        if string[end].isupper():
            upper = True
        elif string[end].islower():
            lower = True
        elif string[end].isdigit():
            digit = True

        if upper and lower and digit:
            maxLen = max(maxLen, end - start + 1)

        while string[end] in charSet:
            if string[start].isupper():
                upper = False
            elif string[start].islower():
                lower = False
            elif string[start].isdigit():
                digit = False
            charSet.remove(string[start])
            start += 1

        charSet.add(string[end])
        end += 1

    return maxLen