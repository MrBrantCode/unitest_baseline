"""
QUESTION:
Design a function `count_char_pairs(text, target_pair)` that calculates the frequency of a unique character pair in a given text string. The function should take two parameters: `text` (the input string) and `target_pair` (the character pair to be searched). It should return the number of times the `target_pair` appears in the `text`.
"""

def count_char_pairs(text, target_pair):
    count = 0

    # Iterate through the string except for the last character
    for i in range(len(text) - 1):
        # Check if the current character and the next one form the target pair
        if text[i] + text[i + 1] == target_pair:
            count += 1
    
    return count