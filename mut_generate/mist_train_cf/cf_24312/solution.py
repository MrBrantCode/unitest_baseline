"""
QUESTION:
Write a function `find_palindrome_pairs` that takes a list of words as input and returns all pairs of distinct indices (i, j) in the list such that the concatenation of the words at these indices (words[i] + words[j]) forms a palindrome.
"""

def find_palindrome_pairs(words): 
    res = [] 
    for i in range(len(words)): 
  
        for j in range(len(words)): 
            if i != j: 
                word = words[i] + words[j] 
                if word == word[::-1]: 
                    res.append((i, j)) 
    return res