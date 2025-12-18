"""
QUESTION:
Write a function `count_words(sentence)` that takes a string as input, splits it into substrings separated by ":", and counts the number of words in each substring. The function should return the sum of the word counts across all substrings, excluding any words with fewer than 3 characters. If any substring contains a word with fewer than 3 characters, return -1. The input string may have leading or trailing whitespaces, which should be trimmed before processing.
"""

def count_words(sentence):
    # Split the sentence on the separator ":"
    substrings = sentence.split(":")
    
    # Initialize a variable to store the sum of word counts
    word_count_sum = 0
    
    # Iterate over each substring
    for substring in substrings:
        # Trim leading and trailing whitespaces
        trimmed_substring = substring.strip()
        
        # Split the substring into words
        words = trimmed_substring.split()
        
        # Initialize a variable to store the count of words in the substring
        word_count = 0
        
        # Iterate over each word
        for word in words:
            # Check if the word has at least 3 characters
            if len(word) >= 3:
                word_count += 1
            else:
                # Return -1 if any word has less than 3 characters
                return -1
        
        # Add the count of words in the substring to the sum
        word_count_sum += word_count
    
    # Return the sum of word counts
    return word_count_sum