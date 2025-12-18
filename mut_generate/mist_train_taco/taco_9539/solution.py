"""
QUESTION:
In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, the sequence BDF is a subsequence of ABCDEF. A substring of a string is a continuous subsequence of the string. For example, BCD is a substring of ABCDEF.

You are given two strings s_1, s_2 and another string called virus. Your task is to find the longest common subsequence of s_1 and s_2, such that it doesn't contain virus as a substring.


-----Input-----

The input contains three strings in three separate lines: s_1, s_2 and virus (1 ≤ |s_1|, |s_2|, |virus| ≤ 100). Each string consists only of uppercase English letters.


-----Output-----

Output the longest common subsequence of s_1 and s_2 without virus as a substring. If there are multiple answers, any of them will be accepted. 

If there is no valid common subsequence, output 0.


-----Examples-----
Input
AJKEQSLOBSROFGZ
OVGURWZLWVLUXTH
OZ

Output
ORZ

Input
AA
A
A

Output
0
"""

def find_longest_common_subsequence_without_virus(s1, s2, virus):
    n, m, v = len(s1), len(s2), len(virus)
    
    # Precompute the next suffix array for the virus string
    next_suffix = [v for i in range(v)]
    for i in range(v - 2, -1, -1):
        j = next_suffix[i + 1]
        while j <= v - 1 and virus[j] != virus[i + 1]:
            j = next_suffix[j]
        next_suffix[i] = j - 1
    
    # Memoization decorator
    def memoize(function):
        memo = dict()
        def memoized(*args):
            if args in memo:
                return memo[args]
            ans = function(*args)
            memo[args] = ans
            return ans
        return memoized
    
    # Recursive function to find the longest common subsequence
    @memoize
    def lcs(i, j, k):
        if k < 0:
            return (float('-inf'), '')
        if i < 0 or j < 0:
            return (0, '')
        if s1[i] == s2[j]:
            if s1[i] != virus[k]:
                newk = k
                while newk < v and virus[newk] != s1[i]:
                    newk = next_suffix[newk]
                r = lcs(i - 1, j - 1, newk - 1)
                return (r[0] + 1, r[1] + s1[i])
            else:
                r1 = lcs(i - 1, j - 1, k - 1)
                r1 = (r1[0] + 1, r1[1] + s1[i])
                r2 = lcs(i - 1, j - 1, k)
                return max(r1, r2, key=lambda x: x[0])
        return max(lcs(i, j - 1, k), lcs(i - 1, j, k), key=lambda x: x[0])
    
    # Get the result
    result = lcs(n - 1, m - 1, v - 1)
    
    # Return the length and the subsequence
    return result

# Example usage:
# result = find_longest_common_subsequence_without_virus("AJKEQSLOBSROFGZ", "OVGURWZLWVLUXTH", "OZ")
# print(result)  # Output: (3, 'ORZ')