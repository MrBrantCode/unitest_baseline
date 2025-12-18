"""
QUESTION:
Write a function `compare_strings` that takes two string parameters and returns "bigger", "smaller", or "equal" depending on the lexicographical order of the reversed strings. The comparison should be case-sensitive and consider spaces and special characters based on their ASCII or Unicode values.
"""

def compare_strings(string1, string2):
    reversed1 = string1[::-1]
    reversed2 = string2[::-1]

    if reversed1 > reversed2:
        return "bigger"
    elif reversed1 < reversed2:
        return "smaller"
    else:
        return "equal"