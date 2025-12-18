"""
QUESTION:
For every string given as input, you need to tell us the number of subsequences of it that are palindromes (need not necessarily be distinct). Note that the empty string is not a palindrome. 

SAMPLE INPUT
1
aab

SAMPLE OUTPUT
4

Explanation

the palindromic subsequences of "aab" are:
"a", "a", "b", "aa", and the method returns 4.
"""

def count_palindromic_subsequences(s: str) -> int:
    n = len(s)
    pali_count = [[0] * n for _ in range(n)]
    
    def c_palis(i: int, j: int) -> int:
        if j < i:
            return 0
        if i == j:
            return 1
        if pali_count[i][j]:
            return pali_count[i][j]
        
        su = c_palis(i, j - 1)
        for k in range(i, j + 1):
            if s[k] == s[j]:
                su += 1 + c_palis(k + 1, j - 1)
        
        pali_count[i][j] = su
        return su
    
    return c_palis(0, n - 1)