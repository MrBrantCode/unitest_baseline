"""
QUESTION:
Create a function `substrings(S)` that takes an alphanumeric string `S` as input, where `1 <= len(S) <= 1000` and `S[i]` is composed solely of lowercase English alphabets. The function should return a dictionary where the keys represent the substrings that consist exclusively of a single unique character and the values denote their corresponding occurrence counts.
"""

def substrings(S):
    result = {}
    size = len(S)
    
    i = 0  
    while i < size:
        j = i   
        while j < size:
            if S[i] != S[j]:
                break
            j += 1
            
        # Found a substring from i to j-1
        for k in range(i, j):
            subs = S[i:j-k+i]
            if len(set(subs)) == 1: # Ensure the substring consists of a single unique character
                if subs not in result:
                    result[subs] = 0
                result[subs] += 1
            
        i = j
        
    return result