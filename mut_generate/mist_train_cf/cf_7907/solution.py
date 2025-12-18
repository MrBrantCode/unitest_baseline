"""
QUESTION:
Write a function called `find_consonant_positions` that takes a string as input and returns the positions of all consonants (excluding 's') that are not adjacent to any vowels. The positions should be sorted in ascending order, and each position should be separated by a comma. The string only contains lowercase English letters.
"""

def find_consonant_positions(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    positions = [str(i) for i in range(len(s)) if s[i] in consonants and 
                 (i == 0 or s[i-1] not in vowels) and (i == len(s)-1 or s[i+1] not in vowels)]
    return ','.join(sorted(positions))