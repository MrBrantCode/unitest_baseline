"""
QUESTION:
Write a function called `process_strings` that takes an array of strings as input and returns three lists of strings. The function should exclude any strings containing the phrase "not only" and categorize the remaining strings into two groups: one containing strings with any form of negation phrases ("no", "not", "never", "none") and the other containing strings without these phrases. The function must have an optimized time complexity to handle large arrays efficiently.
"""

def process_strings(arr):
    negations = ["no", "not", "never", "none"]
    notonly_strings = []
    negation_strings = []
    normal_strings = []

    for string in arr:
        if "not only" in string:
            notonly_strings.append(string)
        elif any(negation in string for negation in negations):
            negation_strings.append(string)
        else:
            normal_strings.append(string)

    return notonly_strings, negation_strings, normal_strings