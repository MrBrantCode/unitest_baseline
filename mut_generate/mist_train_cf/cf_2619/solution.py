"""
QUESTION:
Write two functions, `remove_punctuation` and `count_word_frequency`, that take a string as input. `remove_punctuation` should return the string with all punctuation marks removed except for hyphens and apostrophes, and converted to lowercase. `count_word_frequency` should return a dictionary with the frequency of each word in the string, excluding stop words like "and", "the", and "is". Do not use any built-in functions or libraries for these tasks.
"""

def remove_punctuation(s):
    punctuation_marks = [",", ".", "!", "?", ";", ":", "\"", "(", ")", "[", "]", "{", "}", "<", ">"]
    lowercase_string = ""
    for char in s:
        if char not in punctuation_marks and char != "'":
            lowercase_string += char.lower()
        else:
            if char == "'":
                lowercase_string += char
    return lowercase_string

def count_word_frequency(s):
    stop_words = ["and", "the", "is"]
    word_frequency = {}
    words = s.split()
    for word in words:
        if word not in stop_words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    return word_frequency