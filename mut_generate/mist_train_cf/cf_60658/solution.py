"""
QUESTION:
Create a function `find_smallest_and_most_frequent(seq1, seq2)` that receives two unique sequences of Unicode characters as input and returns the most frequent character from the sequence with the smallest number of unique characters. If there's a tie in the smallest number of unique characters, return the most frequent character from the sequence with the highest frequency. If there's still a tie, return the most frequent character from the second sequence. The function should handle a wide range of Unicode characters, including non-English characters, special symbols, and emojis.
"""

from collections import Counter

def find_smallest_and_most_frequent(seq1, seq2):
    counter1 = Counter(seq1)
    counter2 = Counter(seq2)
    
    if len(counter1) < len(counter2):
        most_common = counter1.most_common(1)
    elif len(counter2) < len(counter1):
        most_common = counter2.most_common(1)
    else:   # Here we handle the tie in the smallest number of unique characters
        most_common1 = counter1.most_common(1)
        most_common2 = counter2.most_common(1)
        if most_common1[0][1] > most_common2[0][1]:
            most_common = most_common1
        else:   # Here we handle the tie in the most frequent character
            most_common = most_common2
    
    return most_common[0][0]