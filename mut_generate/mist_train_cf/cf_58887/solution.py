"""
QUESTION:
Create a function named `magicalString` that takes an integer `n` as input, where `n` will not exceed 10,000,000. The function should return the number of '1's in the first `n` numbers of a magical string `S` that consists of '1', '2', '3', '4', '5' and obeys a specific pattern where concatenating the number of contiguous occurrences of characters generates the string itself. The solution should aim to achieve O(N) time complexity and O(1) space complexity.
"""

def magicalString(n):
    S = [1, 2, 2]
    idx = 2
    while len(S) < n:
        if S[idx] == 1:
            S.append(3 - S[-1])
        else:
            S += [3 - S[-1]] * 2 
        idx += 1
    return S[:n].count(1)