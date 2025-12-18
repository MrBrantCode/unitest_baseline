"""
QUESTION:
Write a function named `word_count` that takes a string as input and returns a dictionary where each unique word in the string is a key and its corresponding value is the number of times it appears in the string. The function should ignore punctuation marks and treat uppercase and lowercase letters as the same. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def word_count(string):
    # Remove punctuation marks and convert string to lowercase
    string = string.lower()
    string = ''.join(c for c in string if c.isalnum() or c.isspace())
    
    # Split the string into words
    words = string.split()
    
    # Create a dictionary to store word counts
    word_counts = {}
    
    # Count the number of occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts