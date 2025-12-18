"""
QUESTION:
Write a function named `remove_longest_word` that takes a sentence as input and returns the string with all occurrences of the longest word(s) removed. The function should handle cases with punctuation marks and special characters, and should not use any built-in functions or libraries that directly solve the problem. The time complexity of the function should be O(n), where n is the length of the sentence. If there are multiple words with the same length as the longest word, all of them should be removed. If there are no words in the sentence, an empty string should be returned.
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