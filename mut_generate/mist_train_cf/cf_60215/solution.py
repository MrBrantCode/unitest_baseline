"""
QUESTION:
Complete the function `advanced_histogram(test)` to process a string of space-separated characters (including uppercase and lowercase letters, numbers, and punctuation marks). The function should return a dictionary containing characters with the highest frequency, with letters in lowercase. If multiple characters have the same highest frequency, return all of them. The function should ignore case for letters, treating 'A' and 'a' as the same character.
"""

def advanced_histogram(test):
    count = {}
    max_count = 0
    result = {}
    
    for char in test:
        if char != ' ':
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