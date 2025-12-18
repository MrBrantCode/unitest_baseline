"""
QUESTION:
Create a function `count_frequency` that takes a string of sentences as input and returns a dictionary where each unique word in the string corresponds to a key and the frequency of its occurrence corresponds to the value. The function should ignore punctuation and consider words with different capitalization as the same word. Additionally, it should treat words that end with 'ing' or 's' as the same word (e.g., 'test', 'testing', and 'tests' are considered the same key).
"""

import string

def count_frequency(my_string):
    # convert to lower case and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    my_string = my_string.lower().translate(translator)

    my_dict = {}
    words = my_string.split(' ')
    for word in words:
        if word[-3:] == 'ing':
            word = word[:-3]
        elif word[-1:] == 's':
            word = word[:-1]
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict