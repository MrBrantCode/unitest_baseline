"""
QUESTION:
Create a function `modify_repeated_words(s)` that takes a string `s` as input and returns a string where each repeated word has its occurrence number as a suffix each time it appears after the first time, while maintaining the original order of words. The word count should start from 2.
"""

def modify_repeated_words(s):
    word_list = s.split()
    word_dict = {}
    result = []

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
            result.append(word + str(word_dict[word]))
        else:
            word_dict[word] = 0
            result.append(word)

    return " ".join(result)