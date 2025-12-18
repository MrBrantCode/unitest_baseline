"""
QUESTION:
Extract all palindromic numerical sequences from a given alphanumeric text. The function should identify a palindromic sequence as a sequence of digits that reads the same backward as forward, and it should not recognize multiple palindromes inside a longer numeric sequence. 

Write a function `extract_palindromes(text)` that takes a string `text` as input and returns a list of all palindromic numerical sequences in the string.
"""

import re

def extract_palindromes(text):
    # Extract all number sequences first
    number_sequences = re.findall(r'\d+', text)
    
    # Then check and collect those that are palindromes
    palindromic_seqs = [seq for seq in number_sequences
                                  if seq == seq[::-1]]  # A string equals to its reverse -> it's a palindrome.
    
    return palindromic_seqs