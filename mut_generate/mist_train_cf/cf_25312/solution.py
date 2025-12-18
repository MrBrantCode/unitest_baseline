"""
QUESTION:
Write a function `find_sum` that takes a list of words as input. Replace each character in the words with its corresponding number in the English alphabet (where 'a' is 1, 'b' is 2, and so on), and return the total sum of these numbers. The input list contains only lowercase English letters.
"""

def find_sum(words):
    total_sum = 0 
    for word in words: 
        for c in word:
            total_sum += ord(c) - 96
    return total_sum