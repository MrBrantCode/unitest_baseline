"""
QUESTION:
Create a function named `word_freq` that receives a sequence of characters as input and returns a dictionary where keys are the words that surpass a length of five characters along with their frequency in the sequence. The function should split the input sequence into words and only consider words with more than five characters. The function should return a dictionary with word frequencies, but it should not contain any words with five or fewer characters.
"""

def word_freq(sequence):
    word_list = sequence.split()
    freq_dict = {}

    for word in word_list:
        if len(word) > 5:
            if word not in freq_dict:
                freq_dict[word] = 1
            else:
                freq_dict[word] += 1

    return freq_dict