"""
QUESTION:
Design a function named `character_pair_frequency` that takes two inputs: a text string and a list of character pairs. The function should return a dictionary showing each character pair's frequency in the given text string and a list of pairs which only appear once. The function should assume that the input text string and character pairs are non-empty and that all character pairs are of length 2.
"""

def character_pair_frequency(text, pairs):
    # Create a dictionary to store the counts of each character pair
    counts = dict.fromkeys(pairs, 0)
    
    # Check each character pair in the text and increment the count in the dictionary
    for pair in pairs:
        counts[pair] = text.count(pair)
        
    # Create a list of unique pairs (pairs that appear only once in the text)
    unique_pairs = [pair for pair, count in counts.items() if count == 1]
    
    # Return the counts dictionary and the list of unique pairs
    return counts, unique_pairs