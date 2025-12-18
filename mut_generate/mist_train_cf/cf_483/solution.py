"""
QUESTION:
Write a function `remove_longest_word(sentence)` that takes a sentence as input and returns a new string with all occurrences of the longest word(s) removed. The function should ignore punctuation and special characters when calculating the length of words. If there are multiple words with the same length as the longest word, remove all of them. If there are no words in the sentence, return an empty string. The function should have a time complexity of O(n), where n is the length of the sentence, and should not use any built-in functions or libraries that directly solve the problem.
"""

def remove_longest_word(sentence):
    words = sentence.split(" ")
    
    # Find the length of the longest word
    max_length = 0
    for word in words:
        length = 0
        for char in word:
            if char.isalpha():
                length += 1
        if length > max_length:
            max_length = length
    
    # Remove all words with the longest length
    result = ""
    for word in words:
        length = 0
        for char in word:
            if char.isalpha():
                length += 1
        if length != max_length:
            result += word + " "
    
    return result.strip()