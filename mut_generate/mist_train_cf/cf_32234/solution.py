"""
QUESTION:
Create a function `wordFrequency` that takes a string `s` as input and returns a dictionary where the keys are the unique words in the input string and the values are the frequencies of those words. The function should consider word case and treat punctuation as part of a word.
"""

def wordFrequency(s: str) -> dict:
    word_list = s.split()  
    frequency_dict = {}  

    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1  
        else:
            frequency_dict[word] = 1  

    return frequency_dict