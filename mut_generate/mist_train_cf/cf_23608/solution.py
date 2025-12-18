"""
QUESTION:
Create a function called `word_count` that takes a string as input and returns a dictionary where each key is a word from the string and the corresponding value is the frequency of that word in the string. The function should consider each word to be separated by a space and should be case-sensitive.
"""

def word_count(my_string): 
    words = my_string.split()  
    frequency = {} 
    for word in words: 
        if word in frequency: 
            frequency[word] += 1
        else: 
            frequency[word] = 1
    return frequency