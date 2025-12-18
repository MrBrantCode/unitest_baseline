"""
QUESTION:
Write a function `smallestSubsequence(s)` that generates the lexicographically smallest subsequence from a given string `s` that includes all unique characters of `s` exactly once. The input string `s` consists of lowercase English alphabets and its length is within the range `1 <= s.length <= 1000`.
"""

def smallestSubsequence(s):
    count = [0]*26
    for char in s:
        count[ord(char)-ord('a')] += 1

    result = [0]*26
    stack = []

    for char in s:
        index = ord(char)-ord('a')
        count[index] -= 1
        if result[index] != 0:
            continue
        while len(stack)>0 and char < stack[-1] and count[ord(stack[-1])-ord('a')] != 0:
            result[ord(stack.pop())-ord('a')] = 0
        stack.append(char)
        result[index] = 1

    return "".join(stack)