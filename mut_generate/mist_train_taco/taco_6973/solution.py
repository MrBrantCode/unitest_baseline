"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a string $S$ with length $N$ and you should change it to a palindrome using a sequence of zero or more operations. In one operation, you should choose two adjacent elements of $S$ (two characters) and swap them; however, neither of these elements may be used in any other operation.

Find the minimum number of operations you have to perform in order to change the string $S$ into a palindrome, or determine that it is impossible.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains a single string $S$ with length $N$.

------  Output ------
For each test case:
If it is impossible to make the string $S$ a palindrome, print a single line containing the string "NO" (without quotes).
Otherwise, print two lines. The first of these lines should contain the string "YES" (without quotes). The second line should contain a single integer ― the minimum required number of operations.

------  Constraints ------
$1 ≤ T ≤ 10,000$
$1 ≤ N ≤ 10^{5}$
$S$ contains only lowercase English letters
the sum of $N$ over all test cases does not exceed $10^{6}$

------  Subtasks ------
Subtask #1 (50 points):
$N ≤ 10^{3}$
$S$ contains only characters 'a' and 'b'
the sum of $N$ over all test cases does not exceed $10^{4}$

Subtask #2 (50 points): original constraints

----- Sample Input 1 ------ 
3

4

abab

5

acbba

5

aaaab
----- Sample Output 1 ------ 
YES

1

YES

1

NO
"""

def min_operations_to_palindrome(S, N):
    i, j = 0, N - 1
    count = 0
    flag = 0
    bl, br = 0, 0
    s = list(S)
    
    while i < N and j >= 0 and i < j:
        if s[i] != s[j]:
            if i + 1 == j:
                flag += 1
                return ("NO", None)
            elif br == 0 and s[i] == s[j - 1]:
                s[j - 1], s[j] = s[j], s[j - 1]
                count += 1
                bl, br = 0, 1
            elif bl == 0 and s[i + 1] == s[j]:
                s[i], s[i + 1] = s[i + 1], s[i]
                count += 1
                bl, br = 1, 0
            else:
                flag += 1
                return ("NO", None)
        else:
            bl, br = 0, 0
        i += 1
        j -= 1
    
    if flag == 0:
        return ("YES", count)