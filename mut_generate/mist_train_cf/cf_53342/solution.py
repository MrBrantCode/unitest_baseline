"""
QUESTION:
Write a function `findRepeatedDnaSequences(s)` that takes a string `s` representing a DNA sequence as input and returns a list of all 10-letter-long sequences (substrings) that occur more than once in the DNA molecule. The input string `s` is composed of the characters 'A', 'C', 'G', and 'T' and has a length between 1 and 10^5.
"""

def findRepeatedDnaSequences(s):
    if len(s) <= 10: return []
    
    sequences, repeat = set(), set()
    
    for i in range(len(s)-9):
        seq = s[i:i+10]
        
        if seq in sequences:
            repeat.add(seq)
        else:
            sequences.add(seq)
    
    return list(repeat)