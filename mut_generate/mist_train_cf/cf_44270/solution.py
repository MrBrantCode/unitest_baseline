"""
QUESTION:
Write a function named `robust_histogram` that takes a string as input and returns a dictionary containing the highest frequency character(s) in lowercase for alphabetic letters, digits, and symbols, along with their count. The function should handle null or invalid inputs by returning `None` for non-string types and an empty dictionary for an empty string. In case of a tie in the frequency, the function should return all the tied characters.
"""

def robust_histogram(test):
    if not isinstance(test, str):
        return None if test is not None else {}
    
    count = {}
    for char in test:
        if char != ' ':
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1

    max_val = max(count.values()) if count else 0  
    result = {key: value for key, value in count.items() if value == max_val}
    return result