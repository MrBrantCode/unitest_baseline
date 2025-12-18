"""
QUESTION:
Vasya is preparing a contest, and now he has written a statement for an easy problem. The statement is a string of length $n$ consisting of lowercase Latin latters. Vasya thinks that the statement can be considered hard if it contains a subsequence hard; otherwise the statement is easy. For example, hard, hzazrzd, haaaaard can be considered hard statements, while har, hart and drah are easy statements. 

Vasya doesn't want the statement to be hard. He may remove some characters from the statement in order to make it easy. But, of course, some parts of the statement can be crucial to understanding. Initially the ambiguity of the statement is $0$, and removing $i$-th character increases the ambiguity by $a_i$ (the index of each character is considered as it was in the original statement, so, for example, if you delete character r from hard, and then character d, the index of d is still $4$ even though you delete it from the string had).

Vasya wants to calculate the minimum ambiguity of the statement, if he removes some characters (possibly zero) so that the statement is easy. Help him to do it!

Recall that subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.


-----Input-----

The first line contains one integer $n$ ($1 \le n \le 10^5$) — the length of the statement.

The second line contains one string $s$ of length $n$, consisting of lowercase Latin letters — the statement written by Vasya.

The third line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 998244353$).


-----Output-----

Print minimum possible ambiguity of the statement after Vasya deletes some (possibly zero) characters so the resulting statement is easy.


-----Examples-----
Input
6
hhardh
3 2 9 11 7 1

Output
5

Input
8
hhzarwde
3 2 6 9 4 8 7 1

Output
4

Input
6
hhaarr
1 2 3 4 5 6

Output
0



-----Note-----

In the first example, first two characters are removed so the result is ardh.

In the second example, $5$-th character is removed so the result is hhzawde.

In the third example there's no need to remove anything.
"""

def minimum_ambiguity_to_avoid_hard(n: int, s: str, a: list) -> int:
    """
    Calculates the minimum ambiguity of the statement after removing some characters
    to ensure the statement does not contain the subsequence 'hard'.

    Parameters:
    - n (int): The length of the statement.
    - s (str): The statement string.
    - a (list): The list of integers representing the ambiguity costs for each character.

    Returns:
    - int: The minimum possible ambiguity of the statement.
    """
    c2c = {c: i for (i, c) in enumerate('hard')}
    dp = [0] * 4 + [10 ** 19]
    
    for i, c in enumerate(s):
        if c in 'hard':
            idx = c2c[c]
            dp[idx] = min(dp[idx] + a[i], dp[idx - 1])
    
    return min(dp)