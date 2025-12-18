"""
QUESTION:
Write a function `analyze_string` that takes a string as input and returns a list of tuples, where each tuple contains a character and its frequency. The function should exclude whitespace and punctuation from the input string, count the occurrences of each character, and sort the characters in descending order based on their frequency. The input string will only contain lowercase and uppercase letters.
"""

def analyze_string(string):
    # Remove whitespace and punctuation
    string = ''.join(ch for ch in string if ch.isalpha())
    
    # Count the occurrences of each character
    char_count = {}
    for ch in string:
        char_count[ch] = char_count.get(ch, 0) + 1
    
    # Sort the characters based on their frequency in descending order
    sorted_chars = sorted(char_count.keys(), key=lambda ch: char_count[ch], reverse=True)
    
    return [(ch, char_count[ch]) for ch in sorted_chars]