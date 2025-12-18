"""
QUESTION:
Write a function `extract_unique_values` that takes a list of tuples as input, extracts unique values from the list based on the second element of each tuple, and sorts them alphabetically. The function should only consider tuples where the first element starts with a vowel.
"""

def extract_unique_values(tuples_list):
    unique_values = []
    for item in tuples_list:
        if item[0][0].lower() in ['a', 'e', 'i', 'o', 'u']:
            if item[1] not in unique_values:
                unique_values.append(item[1])
    unique_values.sort()
    return unique_values