"""
QUESTION:
Given a string S made of letters a, b and c, find the number of sub strings that do not contain all the letters a, b and c. That is the number of sub strings that do not contain at least one of the letters a or b or c.

Note that the sub string should contain atleast one letter, that is it should not be empty string.

Input
First line of the input is the number of test cases T.  It is followed by T lines. Each test case is a single line which is the string S.

Output 
For each test case, print a single number, the required answer. 

Constraints 
1 ≤ |S| ≤ 10^6

SAMPLE INPUT
3
ababa
abc
babac

SAMPLE OUTPUT
15
5
12
"""

def count_substrings_without_all_letters(S: str) -> int:
    L = len(S)
    ans = L * (L + 1) // 2  # Total number of substrings

    a = 0
    b = 0
    c = 0

    for i in range(L):
        if S[i] == 'a':
            a = i + 1
            ans -= min(b, c)
        elif S[i] == 'b':
            b = i + 1
            ans -= min(c, a)
        elif S[i] == 'c':
            c = i + 1
            ans -= min(a, b)

    return ans