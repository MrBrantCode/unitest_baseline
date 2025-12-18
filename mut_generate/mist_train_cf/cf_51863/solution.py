"""
QUESTION:
Create a function `advanced_histogram(test)` that takes a string of space-separated characters, including uppercase and lowercase letters, digits, and symbols. The function should return a dictionary containing the highest frequency character(s) in lowercase format for alphabetic letters, along with their respective count. In case of a tie in frequency, return all tied characters. The function should ignore case for alphabetic letters, but treat digits and symbols as distinct entities.
"""

def advanced_histogram(test):
    # count all character in the test
    count = {}
    for char in test:
        if char != ' ':
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1
                
    # find the maximum frequency
    max_freq = max(count.values()) if count else 0

    # return only the characters with the maximum frequency
    return {char: count for char, count in count.items() if count == max_freq}