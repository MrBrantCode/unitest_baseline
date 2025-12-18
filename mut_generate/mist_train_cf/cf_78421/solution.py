"""
QUESTION:
Given a string `s` of length `n` consisting of characters 'D' and 'I', find the smallest lexicographical permutation of the array `[1, 2, ..., n+1]` that corresponds to the cipher `s`, where 'D' signifies a descending correlation and 'I' signifies an ascending correlation. The length of `s` is a positive integer and will not exceed 10,000. Implement a function `findPermutation(s)` to solve this problem.
"""

def findPermutation(s):
    ans, stack, j = [], [], 0
    for i in range(len(s)):
        if s[i] == 'I':
            stack.append(i+1)
            while stack:
                ans.append(stack.pop())
        else:
            stack.append(i+1)
    stack.append(len(s)+1)
    while stack:
        ans.append(stack.pop())
    return ans