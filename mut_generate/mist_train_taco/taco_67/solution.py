"""
QUESTION:
Given a string, find the longest substring which is palindrome in Linear time O(N).
Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow. The only line of each test case contains a string.
Output:
For each test case print the Longest Palindromic Substring. If there are multiple such substrings of same length, print the one which appears first in the input string.
Constraints:
1 <= T <= 100
1 <= N <= 50
Example:
Input:
2
babcbabcbaccba
forgeeksskeegfor
Output:
abcbabcba
geeksskeeg
 
 
 
Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""

def find_longest_palindrome_substring(text: str) -> str:
    def manacher_odd(s: str) -> str:
        n = len(s)
        s = '$' + s + '^'
        p = [0] * (n + 2)
        (l, r) = (1, 1)
        max_len = 0
        pos = -1
        for i in range(1, n + 1):
            p[i] = max(0, min(r - i, p[l + r - i]))
            while s[i - p[i]] == s[i + p[i]]:
                p[i] += 1
            if p[i] > max_len:
                max_len = p[i]
                pos = i
            if i + p[i] > r:
                r = i + p[i]
                l = i - p[i]
        return s[pos - p[pos] + 2:pos + p[pos] - 1]

    # Preprocess the string to handle even-length palindromes
    s = '#' + '#'.join(list((c for c in text))) + '#'
    ans = manacher_odd(s)
    return ''.join(ans.split(sep='#'))