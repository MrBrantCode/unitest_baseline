"""
QUESTION:
Create a function named `mirror_alternate` that takes a string as input. The function should reverse every other word in the string, starting from the second word (index 1), and return the modified string. The words are separated by spaces and there are no punctuation or special characters in the string.
"""

def mirror_alternate(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 != 0:  
            words[i] = words[i][::-1]
    return ' '.join(words)