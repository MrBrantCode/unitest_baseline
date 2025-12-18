"""
QUESTION:
Given two strings A and B, you need to find the last occurrence ( 1 based indexing) of string B in string A.
 
Example 1:
Input:
A = abcdefghijklghifghsd
B = ghi
Output:
13
Explanation:
ghi occurs at position 13 for the
last time in string A.
Example 2:
Input:
A = abdbccaeab
B = abc
Output:
-1
Explanation:
abc is not a substring of A
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findLastOccurence() which takes two strings A and B as input parameters and returns the position of the last occurrence of B in A. If B is not present in A, return -1.
 
Expected Time Complexity: O(len(A))
Expected Space Complexity: O(len(A))
 
Constarints:
1<=T<=100
1<=len(B)<=10^{5}
1<=len(A)<=10^{6}
len(A)>=len(B)
"""

def find_last_occurrence(A: str, B: str) -> int:
    c = -1
    m = len(B)
    n = len(A)
    lps = [0] * m
    x = 1
    l = 0
    
    # Construct the LPS array
    while x < m:
        if B[x] == B[l]:
            l += 1
            lps[x] = l
            x += 1
        elif l > 0:
            l = lps[l - 1]
        else:
            lps[x] = 0
            x += 1
    
    # KMP search to find the last occurrence
    (i, j) = (0, 0)
    while n - i >= m - j:
        if B[j] == A[i]:
            i += 1
            j += 1
        if j == m:
            c = i - j
            j = lps[j - 1]
        elif i < n and B[j] != A[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    if c == -1:
        return -1
    return c + 1