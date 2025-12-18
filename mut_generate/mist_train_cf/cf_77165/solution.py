"""
QUESTION:
Write a function `find_longest_subsequence(sequence)` that uses dynamic programming to find the length of the longest continuously ascending subsequence within a given numerical array `sequence`. A continuously ascending subsequence is one where each element is greater than the previous one. The function should be able to handle negative numbers, zeros, and duplicate numbers, which are considered non-ascending.
"""

def find_longest_subsequence(sequence):
    if len(sequence) == 0:  
        return 0
 
    dp = [1]*len(sequence)  
    max_length = 1  
    
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if (sequence[i] > sequence[j]) and (dp[i] < dp[j] + 1):
                dp[i] = dp[j]+1
 
        if dp[i] > max_length:
            max_length = dp[i]
 
    return max_length