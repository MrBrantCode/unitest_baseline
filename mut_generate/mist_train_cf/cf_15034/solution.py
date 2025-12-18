"""
QUESTION:
Write a function called `find_most_frequent_word` that takes a string as input and returns the word with the maximum frequency. If multiple words have the same maximum frequency, return the word that occurs first in the string. The function should be case-insensitive.
"""

def find_most_frequent_word(sentence):
    # Step 1: Convert the input string to lowercase
    sentence = sentence.lower()

    # Step 2: Split the string into words using whitespace as the delimiter
    words = sentence.split()

    # Step 3: Initialize an empty dictionary to store the frequency of each word
    word_freq = {}

    # Step 4: Iterate over the list of words and update the frequency count in the dictionary
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Step 5: Initialize variables to keep track of the maximum frequency and the word with the maximum frequency
    max_freq = 0
    most_frequent_word = None

    # Step 6: Iterate over the dictionary and update the maximum frequency and the corresponding word if a higher frequency is found
    for word, freq in word_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_word = word

    # Step 7: Output the word with the maximum frequency
    return most_frequent_word