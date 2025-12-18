"""
QUESTION:
Write a function called `string_difference` that takes two text strings as input and returns the difference between the two strings. The function should compare alphanumeric characters and spaces, ignoring special characters and considering characters with different cases as different. If the input strings have different lengths, only consider characters up to the length of the shorter string for comparison. The function should handle Unicode characters in the input strings.
"""

def string_difference(str1, str2):
    diff_count = 0
    for char1, char2 in zip(str1, str2):
        if not char1.isalnum() or not char2.isalnum():
            continue
        if char1 == ' ' or char2 == ' ':
            diff_count += 1
        elif char1 != char2:
            diff_count += 1
    return diff_count