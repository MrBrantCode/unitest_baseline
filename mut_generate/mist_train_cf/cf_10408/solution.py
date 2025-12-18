"""
QUESTION:
Write a function `analyze_string` that takes a string of lowercase and uppercase letters as input, excluding whitespace and punctuation, and returns a list of tuples where each tuple contains a character and its frequency in the string. The list should be sorted in descending order of the character frequencies.
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