"""
QUESTION:
Create a function called `find_consonant_positions` that takes a string `paragraph` as input and returns a dictionary where the keys are consonant characters, and the values are dictionaries containing the positions and frequency of each consonant in the paragraph. The positions should be 0-indexed and the function should be case-sensitive.
"""

def find_consonant_positions(paragraph):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_positions = {}

    for i in range(len(paragraph)):
        if paragraph[i] in consonants:
            if paragraph[i] in consonant_positions:
                consonant_positions[paragraph[i]]["positions"].append(i)
                consonant_positions[paragraph[i]]["frequency"] += 1
            else:
                consonant_positions[paragraph[i]] = {"positions": [i], "frequency": 1}

    return consonant_positions