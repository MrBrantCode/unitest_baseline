"""
QUESTION:
Develop a function called count_palindromes that takes a string of text as input. The function should count the occurrences of unique palindromes in the text, ignoring punctuation, whitespace, and case sensitivity. It should also measure its own execution time and return both the dictionary of palindromes and their counts, and the elapsed time. The function should be able to process a 500-word input string within 2 seconds.
"""

import re
import time

def count_palindromes(text):
    start_time = time.time()
    text = re.sub(r'\W+', ' ', text)  
    words = text.lower().split()  
    palindrome_dict = {}  
    
    for word in words:
        if word == word[::-1]:  
            if word in palindrome_dict:
                palindrome_dict[word] += 1
            else:
                palindrome_dict[word] = 1
    
    elapsed_time = time.time() - start_time
    return palindrome_dict, elapsed_time