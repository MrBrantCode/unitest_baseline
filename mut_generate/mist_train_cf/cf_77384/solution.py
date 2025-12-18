"""
QUESTION:
Create a Python function `count_vowels_in_palindromes` that takes a tuple of strings as input and returns a dictionary where the keys are the palindrome strings and the values are the accumulated count of vowels ('a', 'e', 'i', 'o', 'u') in each key. The function should only include strings that are actual palindromes in the output dictionary.
"""

def count_vowels_in_palindromes(palindrome_tuples):
    vowels = {'a', 'e', 'i', 'o', 'u'}  
    result = {}  

    for word in palindrome_tuples:
        if word == word[::-1]:
            vowel_count = sum(1 for char in word.lower() if char in vowels)
            result[word] = vowel_count
    
    return result