"""
QUESTION:
Implement the function `censor_and_analyze_words(s, target, ratio, frequency, start_char, end_char)`. 

The function should take a compound string `s` made up of words separated by punctuation or whitespace, a target word `target`, a vowel ratio `ratio`, a frequency integer `frequency`, a start character `start_char`, and an end character `end_char`. 

It should disintegrate the string into words, removing all instances of the target word and excluding words that have a vowel ratio greater than or equal to the provided ratio, are more than 6 characters long, appear fewer times than the provided frequency, start with the start character, end with the end character, or are palindromes. 

The function should then reverse the remaining words and return them in alphabetical order.
"""

def censor_and_analyze_words(s, target, ratio, frequency, start_char, end_char):
    """
    Given a compound string made up of words separated by punctuation or whitespace. Your task is to disintegrate the 
    string into words and create a list of these words in the original order, removing all instances of a specific 
    target word. Additionally, these words should then be reversed and returned in alphabetical order.
    
    The function also excludes words that:
    a) Have a ratio of vowels to total letters that is greater or equal to the provided ratio
    b) Are longer than 6 characters
    c) Appear in the string fewer times than the provided 'frequency' number
    d) Start with the character given by 'start_char'
    e) End with the character given by 'end_char'
    f) Are palindromes, meaning they read the same way forwards as they do backwards
    """
    
    # Convert the input string to lower case and split it into words
    words = s.lower().split()
    
    # Initialize a dictionary to store the frequency of each word
    word_frequency = {}
    
    # Initialize an empty list to store the result
    result = []
    
    # Count the frequency of each word
    for word in words:
        word = ''.join(e for e in word if e.isalnum())  # remove punctuation
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    
    # Filter out words based on the given conditions
    for word in word_frequency:
        if (word != target and 
            word_frequency[word] >= frequency and 
            len(word) <= 6 and 
            word[0] != start_char and 
            word[-1] != end_char and 
            word != word[::-1] and 
            sum(1 for char in word if char in 'aeiou') / len(word) < ratio):
            result.append(word[::-1])  # reverse the word
    
    # Return the result in alphabetical order
    return sorted(result)