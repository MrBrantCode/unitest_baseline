"""
QUESTION:
Given the string `croakOfFrogs`, return the minimum number of different frogs to finish all the croak in the given string. Each frog has a distinct sound, represented by a unique character. A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. If the given string is not a combination of valid "croak", return -1. 

Constraints: `1 <= croakOfFrogs.length <= 10^6`, all characters in the string are 'c', 'r', 'o', 'a' or 'k', and each character in the string is unique to a frog. Implement the function `minNumberOfFrogs(croakOfFrogs)`.
"""

def minNumberOfFrogs(croakOfFrogs):
    count = [0] * 5  
    frogs = max_frogs = 0

    for i in croakOfFrogs:
        idx = "croak".find(i)
        
        count[idx] += 1  
        
        if i == 'c':
            frogs += 1
            max_frogs = max(max_frogs, frogs)
        elif i == 'k':
            frogs -= 1
        elif count[idx] > count[idx - 1]:  
            return -1
    if frogs != 0: 
        return -1
    return max_frogs