"""
QUESTION:
Write a function `prime_length_substrings(sentence)` that takes a string of words separated by spaces as input and returns a new string comprising substrings from the original sentence. 

The function should include only substrings with prime lengths and preserve the original sequence, while avoiding repeating characters across substrings. The input sentence should only contain alphabetic characters and have a length between 1 and 500. Spaces may be omitted to form substrings, and the same word from the original sentence should not be repeated in the substring.
"""

def prime_length_substrings(sentence):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    added_words = set() 
    result = []

    for word in words:
        word = ''.join(char for char in word if char.isalpha()) 
        if is_prime(len(word)) and word not in added_words:
            result.append(word)
            added_words.add(word)

    return ' '.join(result)