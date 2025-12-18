"""
QUESTION:
Write a function named `LCSubStr` that takes two string inputs `Str1` and `Str2`. This function should find the length of the longest common subsequence between the two strings. The function should return the length of the longest common subsequence as an integer.
"""

def LCSubStr(Str1, Str2):
    n = len(Str1)
    m = len(Str2)
    LCSuff = [[0 for k in range(m + 1)] for l in range(n + 1)]   
    result = 0    
    for i in range(n): 
        for j in range(m):  
            if (Str1[i] == Str2[j]): 
                LCSuff[i + 1][j + 1] = LCSuff[i][j] + 1
                if (LCSuff[i + 1][j + 1] > result): 
                    result = LCSuff[i + 1][j + 1]
    return result