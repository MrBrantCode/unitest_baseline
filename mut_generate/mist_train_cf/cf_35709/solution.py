"""
QUESTION:
Write a function `categorize_security_strings` that takes a list of strings as input where each string consists of three parts separated by colons (:). The function should categorize the strings into different groups based on the first part of each string (before the first colon) and return a dictionary where the keys are the unique categories and the values are the counts of occurrences of each category. The input list may contain duplicate categories.
"""

def categorize_security_strings(strings):
    categories_count = {}
    for string in strings:
        category = string.split(":")[0]
        if category in categories_count:
            categories_count[category] += 1
        else:
            categories_count[category] = 1
    return categories_count