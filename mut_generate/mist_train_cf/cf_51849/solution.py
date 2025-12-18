"""
QUESTION:
Develop a function `check_sequences(seq1, seq2)` that takes two alpha-numeric sequences as input and returns a tuple containing a boolean indicating whether the sequences are lexical anagrams and the number of unique anagrams that can be formed from each sequence.
"""

from collections import Counter
from math import factorial

def check_sequences(seq1, seq2):
    # Count characters
    counts1 = Counter(seq1)
    counts2 = Counter(seq2)
    
    # Check if character counts match
    are_anagrams = counts1 == counts2
    
    # Calculate factorial of length
    total1 = factorial(sum(counts1.values()))
    total2 = factorial(sum(counts2.values()))
    
    # Divide by factorials of individual character counts
    for count in counts1.values():
        total1 //= factorial(count)
    for count in counts2.values():
        total2 //= factorial(count)
        
    return (are_anagrams, total1, total2)