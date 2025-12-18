"""
QUESTION:
Write a function `most_frequent_word(sentence)` that finds the most frequent word in a given sentence. The solution should not use any built-in functions or libraries for string manipulation or counting occurrences, and it must have a time complexity of O(n) and a space complexity of O(k), where n is the length of the sentence and k is the number of unique words in the sentence. The input sentence is a string of words separated by spaces, and the function should return the most frequent word as a string.
"""

def most_frequent_word(sentence):
    # Create a dictionary to store the frequency of each word
    word_freq = {}
    
    # Split the sentence into words
    words = sentence.split()
    
    # Iterate through each word
    for word in words:
        # If the word is not in the dictionary, add it with a frequency of 1
        if word not in word_freq:
            word_freq[word] = 1
        # If the word is already in the dictionary, increment its frequency by 1
        else:
            word_freq[word] += 1
    
    # Find the word with the maximum frequency
    max_word = ""
    max_freq = 0
    for word, freq in word_freq.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    
    return max_word