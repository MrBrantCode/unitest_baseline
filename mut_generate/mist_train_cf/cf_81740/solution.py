"""
QUESTION:
Given two strings `p` and `q` containing lowercase letters, `'*'`, and `'/'`, determine if they become identical after being processed in empty text editors, where `'*'` represents a duplicate character operation and `'/'` represents a delete character operation. The length of `p` and `q` are between 1 and 200. Implement a function `areProcessedStringsEqual(p: str, q: str) -> bool` that solves this problem in O(n) time and O(1) space.
"""

def entrance(p: str, q: str) -> bool:
    i, j = len(p) - 1, len(q) - 1
    skipP, skipQ = 0, 0

    while i >= 0 or j >= 0:
        while i >= 0:
            if p[i] == '*':
                skipP += 2
                i -= 1
            elif p[i] == '/':
                skipP -= 1
                i -= 1
            elif skipP > 0:
                skipP -= 1
                i -= 1
            else:
                break
                
        while j >= 0:
            if q[j] == '*':
                skipQ += 2
                j -= 1
            elif q[j] == '/':
                skipQ -= 1
                j -= 1
            elif skipQ > 0:
                skipQ -= 1
                j -= 1
            else:
                break
        
        if i >= 0 and j >= 0 and p[i] != q[j]:
            return False
        
        if (i >= 0) != (j >= 0):
            return False

        i -= 1
        j -= 1

    return True