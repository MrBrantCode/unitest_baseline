"""
QUESTION:
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.
Given two anagrams A and B, return the smallest K for which A and B are K-similar.
Example 1:
Input: A = "ab", B = "ba"
Output: 1


Example 2:
Input: A = "abc", B = "bca"
Output: 2


Example 3:
Input: A = "abac", B = "baca"
Output: 2


Example 4:
Input: A = "aabc", B = "abca"
Output: 2



Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
"""

def calculate_k_similarity(A: str, B: str) -> int:
    def dfs(a, b):
        if not a:
            return 0
        one = []
        two = []
        for i in range(len(a)):
            if a[0] == b[i]:
                one.append(i)
                if b[0] == a[i]:
                    two.append(i)
        if two:
            i = two[0]
            c = a[1:i] + a[i + 1:]
            d = b[1:i] + b[i + 1:]
            return dfs(c, d) + 1
        else:
            res = float('inf')
            for i in one:
                c = a[i] + a[1:i] + a[i + 1:]
                d = b[:i] + b[i + 1:]
                res = min(res, dfs(c, d) + 1)
            return res

    a = ''
    b = ''
    for i in range(len(A)):
        if A[i] != B[i]:
            a += A[i]
            b += B[i]
    return dfs(a, b)