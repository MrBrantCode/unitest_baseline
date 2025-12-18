"""
QUESTION:
Create a function `word_freq` that takes a string input and returns a dictionary where each unique word from the input string is a key, and its corresponding value is the frequency of the word's occurrences in the input string. The input string may contain multiple spaces between words, and the function should consider 'hey' and 'Hey' as the same word, but the provided code snippet does not specify this.
"""

def word_freq(input_string):
    # Create an empty dictionary
    freq_dict = {}

    # Split string into list of words
    word_list = input_string.split()

    # Iterate over each word in the list
    for word in word_list:
        word = word.lower()  # Consider 'hey' and 'Hey' as the same word
        if word in freq_dict:
            # If the word is already in the dictionary, increment its count
            freq_dict[word] += 1
        else:
            # If the word is not in the dictionary, add it with a count of 1
            freq_dict[word] = 1

    # Return the completed frequency dictionary
    return freq_dict