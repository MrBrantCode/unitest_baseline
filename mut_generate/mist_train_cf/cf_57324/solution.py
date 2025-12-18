"""
QUESTION:
Write a function `expunge_recurring_chars(str)` that takes a string of alphabetic characters as input and returns a novel string where all recurring, successive characters are replaced with the character and the number of occurrences. The function should handle empty inputs and return an empty string in such cases.
"""

def expunge_recurring_chars(s):
    # Handle the edge case of empty input
    if not s:
        return ''

    result = ''
    count = 1
    i = 1

    while(i <= len(s)):
        if i == len(s) or s[i] != s[i - 1]:
            result += s[i - 1] if count == 1 else s[i - 1] + str(count)
            count = 1
        else:
            count += 1
        i += 1

    return result