"""
QUESTION:
Write a function `custom_histogram` that takes a string of space-separated letters (case insensitive) as input and returns a dictionary of the letters with their maximum counts in lowercase, formatted as 'letter_count'. Ignore special characters. If several letters have the same maximum occurrence, return all of them.
"""

def custom_histogram(s):
    count = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in count:
                count[char_lower] += 1
            else:
                count[char_lower] = 1
    result = {}
    max_count = 0
    for key in count:
        max_count = max(max_count, count[key])
    for key in count:
        if count[key] == max_count:
            result[f"{key}_{count[key]}"] = count[key]
    return result