"""
QUESTION:
Create a function named `advanced_histogram` that takes a string containing a mix of uppercase and lowercase letters, numerals, and special symbols as input. The function should return a dictionary showcasing the highest occurrence character(s) in lowercase, along with their respective count. All characters sharing the peak frequency should be featured. Uppercase and lowercase letters should be treated as the same, and space ' ' should be omitted from the count.
"""

def advanced_histogram(test):
    count = {}
    for char in test:
        if char != ' ':
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1
    
    # find the highest frequency
    max_value = max(count.values()) if count else 0

    # keep only those characters with max value
    return {k: v for k, v in count.items() if v == max_value}