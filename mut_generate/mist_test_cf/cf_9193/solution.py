"""
QUESTION:
Create a function called `find_top_strings` that takes an array of strings as input and returns the top 3 strings with the greatest length. If there are multiple strings with the same length, return them in the order they appear in the array. The function should not take any additional parameters.
"""

def find_top_strings(arr):
    topStrings = []
    maxLength = 0

    for string in arr:
        if len(string) > maxLength:
            maxLength = len(string)
            topStrings = []
            topStrings.append(string)
        elif len(topStrings) < 3 and string not in topStrings and len(string) == maxLength:
            topStrings.append(string)

    return topStrings