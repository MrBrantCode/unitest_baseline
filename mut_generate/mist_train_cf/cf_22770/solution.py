"""
QUESTION:
Create a function named `count_unique_words` that takes a string as input and returns a dictionary with the number of occurrences of each unique word in the string and a list of unique words in descending order of their frequency of occurrence. The function should ignore punctuation and consider words in a case-insensitive manner, and it should not use built-in functions or libraries to solve the problem.
"""

def count_unique_words(string):
    # Convert the string to lowercase and remove punctuation
    string = string.lower()
    string = ''.join(c for c in string if c.isalpha() or c.isspace())
    
    # Split the string into words
    words = string.split()
    
    # Create a dictionary to store the word counts
    word_counts = {}
    
    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort the words by their counts in descending order
    sorted_words = sorted(word_counts.keys(), key=lambda x: word_counts[x], reverse=True)
    
    # Return the word counts and sorted words
    return word_counts, sorted_words