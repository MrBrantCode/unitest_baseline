"""
QUESTION:
Create a function `process_string(s)` that takes a string `s` of comma-separated words, splits it into a list, removes duplicates, sorts the words in alphabetical order, and counts the number of occurrences of each word. The function should return a list of unique sorted words and a dictionary with word counts.
"""

def process_string(s):
    # Split the string into a list of words
    words = [word.strip() for word in s.split(",")]
    # Sort the words
    words.sort()
    # Create a dictionary to store the word counts
    wordCounts = {}
    # Loop over the words
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in wordCounts:
            wordCounts[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            wordCounts[word] = 1
    # Remove duplicates from the word list
    words = list(dict.fromkeys(words))
    # Return the sorted words and the word counts
    return words, wordCounts