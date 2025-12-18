"""
QUESTION:
Ashish has a string $s$ of length $n$ containing only characters 'a', 'b' and 'c'.

He wants to find the length of the smallest substring, which satisfies the following conditions:

Length of the substring is at least $2$

'a' occurs strictly more times in this substring than 'b'

'a' occurs strictly more times in this substring than 'c'

Ashish is busy planning his next Codeforces round. Help him solve the problem.

A string $a$ is a substring of a string $b$ if $a$ can be obtained from $b$ by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.


-----Input-----

The first line contains a single integer $t$ $(1 \le t \le 10^{5})$  — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer $n$ $(2 \le n \le 10^{6})$  — the length of the string $s$.

The second line of each test case contains a string $s$ consisting only of characters 'a', 'b' and 'c'.

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^{6}$.


-----Output-----

For each test case, output the length of the smallest substring which satisfies the given conditions or print $-1$ if there is no such substring.


-----Examples-----

Input
3
2
aa
5
cbabb
8
cacabccc
Output
2
-1
3


-----Note-----

Consider the first test case. In the substring "aa", 'a' occurs twice, while 'b' and 'c' occur zero times. Since 'a' occurs strictly more times than 'b' and 'c', the substring "aa" satisfies the condition and the answer is $2$. The substring "a" also satisfies this condition, however its length is not at least $2$.

In the second test case, it can be shown that in none of the substrings of "cbabb" does 'a' occur strictly more times than 'b' and 'c' each.

In the third test case, "cacabccc", the length of the smallest substring that satisfies the conditions is $3$.
"""

def find_smallest_valid_substring_length(s: str) -> int:
    """
    Finds the length of the smallest substring in the given string 's' that satisfies the following conditions:
    1. The length of the substring is at least 2.
    2. 'a' occurs strictly more times in this substring than 'b'.
    3. 'a' occurs strictly more times in this substring than 'c'.

    Parameters:
    s (str): The input string containing only characters 'a', 'b', and 'c'.

    Returns:
    int: The length of the smallest substring that satisfies the conditions, or -1 if no such substring exists.
    """
    if 'aa' in s:
        return 2
    elif 'aca' in s or 'aba' in s:
        return 3
    elif 'abca' in s or 'acba' in s:
        return 4
    elif 'abbacca' in s or 'accabba' in s:
        return 7
    else:
        return -1