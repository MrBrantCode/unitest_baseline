"""
QUESTION:
Implement a function `count_distinct_words` that takes a string as input and returns the number of distinct words in the string. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in Python functions or libraries for string manipulation or counting.
"""

def count_distinct_words(string):
    distinct_words = {}  
    word_start = 0  

    for i in range(len(string)):
        if string[i] == ' ' or string[i] == '\t' or string[i] == '\n':
            if i > word_start:
                word = string[word_start:i]
                if word not in distinct_words:
                    distinct_words[word] = 1
                else:
                    distinct_words[word] += 1
            word_start = i + 1

    if len(string) > word_start:
        word = string[word_start:]
        if word not in distinct_words:
            distinct_words[word] = 1
        else:
            distinct_words[word] += 1

    return len(distinct_words)