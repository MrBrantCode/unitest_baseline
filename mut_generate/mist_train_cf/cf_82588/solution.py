"""
QUESTION:
Write a function maxProduct that takes an array of strings `words` as input and returns the maximum possible product of the lengths of two words that do not share any common letters. If no such pair exists, return 0. 

The length of `words` is between 2 and 1000 (inclusive), and the length of each word is between 1 and 1000 (inclusive). Each word consists only of lowercase English letters.
"""

def maxProduct(words):
    chars = [0]*len(words)
    for i in range(len(words)):
        for c in words[i]:
            chars[i] |= 1 << (ord(c) - 97)
    
    max_product = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if not (chars[i] & chars[j]):
                max_product = max(max_product, len(words[i])*len(words[j]))
    
    return max_product