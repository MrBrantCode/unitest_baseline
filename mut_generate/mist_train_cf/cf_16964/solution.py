"""
QUESTION:
Write a function `separate_and_count` that takes a string `sentence` as input, separates the words and stores them in an array, counts the number of occurrences of each word in the sentence without using built-in functions or libraries for counting occurrences, and returns the word count in descending order of frequency.
"""

def separate_and_count(sentence):
    """
    Separate the words in a sentence and count the occurrences of each word.
    
    Args:
    sentence (str): The input sentence.
    
    Returns:
    dict: A dictionary where keys are the unique words in the sentence and values are their respective counts in descending order of frequency.
    """
    
    # Remove leading/trailing whitespaces and split the sentence into words
    words = sentence.strip().split()
    
    # Create a dictionary to store word counts
    word_count = {}
    
    # Iterate through each word and update its count
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    # Sort the dictionary by values (counts) in descending order
    sorted_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_count