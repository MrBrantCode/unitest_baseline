"""
QUESTION:
Write a function `find_longest_word(sentence)` that takes a string `sentence` as input and returns a tuple containing the longest word in the sentence and the number of vowels in that word. If multiple words have the same length, the function should return the word with the most vowels. If there is still a tie, the function should return the first word that appears in the sentence. The function should be case-insensitive when counting vowels.
"""

def find_longest_word(sentence):
    words = sentence.split()  
    max_length = 0  
    max_vowels = 0  
    longest_word = ''

    for word in words:  
        num_vowels = sum(1 for char in word if char in 'aeiouAEIOU')  
        if len(word) > max_length or (len(word) == max_length and num_vowels > max_vowels):
            max_length = len(word)
            max_vowels = num_vowels
            longest_word = word
    
    return longest_word, max_vowels