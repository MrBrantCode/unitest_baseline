"""
QUESTION:
Write a function `analyze_repetition_in_string(input_string)` that takes a string as input and returns the most repeated character and the least repeated character along with their counts. The function should disregard spaces and punctuation and handle edge cases like null and empty string input. If there are multiple characters having the same most or least frequency, return any one character.
"""

def analyze_repetition_in_string(input_string):
    if not input_string:  # Catch None and Empty String
        return "Invalid input"

    char_count = dict()
    max_count = 0
    min_count = float('inf')
    max_char = min_char = None

    for char in input_string:
        # Skip spaces and punctuation
        if not char.isalnum():
            continue

        if char not in char_count: 
            char_count[char] = 0
        char_count[char] += 1

        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char

        if char_count[char] < min_count:
            min_count = char_count[char]
            min_char = char
            
    result = f"Most repeated character: {max_char} - Count: {max_count}\n"
    result += f"Least repeated character: {min_char} - Count: {min_count}"
    
    return result