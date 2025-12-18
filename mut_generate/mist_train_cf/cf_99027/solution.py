"""
QUESTION:
Create a function named `last_occurrence` that takes two parameters: `words` (a list of strings) and `substring` (a string). The function should return the index of the last occurrence of a word in the list that contains the specified `substring`. The function must use bitwise operators and have a time complexity of O(n), without relying on any built-in string operations or library functions.
"""

def last_occurrence(words, substring):
    # Convert the substring to a hash value
    sub_hash = 0
    for char in substring:
        sub_hash = sub_hash << 1 | ord(char)
        
    last_index = -1
    for i in range(len(words)):
        word_hash = 0
        for char in words[i]:
            word_hash = word_hash << 1 | ord(char)
            
        # Check if the substring is present in the word
        if (word_hash & ((1 << len(substring)) - 1)) == sub_hash:
            last_index = i
            
    return last_index