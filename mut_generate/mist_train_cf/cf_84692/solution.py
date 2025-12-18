"""
QUESTION:
Write a function `find_characters(word, characters)` that determines which characters from the `characters` string are found in the `word` string and returns their frequency of occurrence. The function should optimize the number of iterations over the `word` string.
"""

def find_characters(word, characters):
    # Build a letter frequency count for the entire word
    word_count = {}
    for char in word:
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    
    # Extract counts for the characters of interest
    count = {}
    for char in characters:
        if char in word_count:
            count[char] = word_count[char]

    return count