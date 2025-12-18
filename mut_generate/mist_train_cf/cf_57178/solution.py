"""
QUESTION:
Create a function `advanced_histogram` that takes a string `test` as input and returns a dictionary where the keys are the characters in the string (except for underscores, which are ignored) and the values are the maximum counts of any character in the string. If multiple characters have the same maximum count, they should all be included in the output dictionary. English alphabetic characters should be converted to lower case before counting.
"""

def advanced_histogram(test):
    count = {}
    max_count = 0
    result = {}
    
    for char in test:
        if char != '_':
            key = char.lower() if char.isalpha() else char
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
            if count[key] > max_count:
                max_count = count[key]
                result = {key: max_count}
            elif count[key] == max_count:
                result[key] = max_count
    
    return result