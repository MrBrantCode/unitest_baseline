"""
QUESTION:
Flamel is making the Elixir of Life but he is missing a secret ingredient, a set of contiguous plants (substring) from the Garden of Eden.
The garden consists of various plants represented by string S, where each letter represents a different plant.  But the prophecy has predicted that the correct set of plants required to make the potion will appear in the same contiguous pattern (substring) at the beginning of the forest (prefix), the end of the forest (suffix), and will also be the most frequent sequence present in the entire forest.
Identify the substring of plants required to make the elixir and find out the number of times it appears in the forest. 
Example 1:
Input: S = "ababaaaab"
Output: 3
Explanation: Substring "ab" is a prefix, 
It is also a suffix and appears 3 times.
Example 2:
Input: S = "aaaa"
Output: 4
Explanation: Substring "aaaa" occurs 1 time, 
Substring "aaa" occurs 2 times, substring 
"aa" occurs 3 times, substring "a" occurs 
4 times. All of them are proper prefixes 
and suffixes. But, "a" has the maximum 
frequency.
Example 3:
Input: S = "abcdef"
Output: 1
Your Task: 
You don't need to read input or print anything. Complete the function maxFrequency() which takes string S as input parameter and returns the frequency of the most frequent substring of S which is also a prefix and suffix of the original string.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints: 
1 ≤ |S| ≤ 10^{5}
"""

def z_function(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    (l, r) = (0, 0)
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            r = i + z[i]
            l = i
    return z

def find_elixir_frequency(S):
    z = z_function(S)
    ans = 0
    n = len(S)
    for i in range(n - 1, -1, -1):
        if z[i] == n - i:
            suffix = S[-z[i]:]
            start = 0
            while True:
                pos = S.find(suffix, start)
                if pos == -1:
                    return ans
                ans += 1
                start = pos + len(suffix)
    return ans