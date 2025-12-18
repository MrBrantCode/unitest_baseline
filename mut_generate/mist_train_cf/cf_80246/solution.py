"""
QUESTION:
Write a function `burrows_wheeler_transform(s)` that takes a string `s` as input and returns its Burrows-Wheeler Transform (BWT). The BWT is obtained by sorting all rotations of `s` in lexicographic order and taking the last character of each sorted rotation. Assume the input string is in lowercase and does not contain special characters.
"""

def burrows_wheeler_transform(s):
    # forming all rotations of the input string
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    
    # sorting all rotations in lexicographic order
    rotations.sort()
    
    # taking the last character of each sorted rotations
    bwt = ''.join(rot[-1] for rot in rotations)
    
    return bwt