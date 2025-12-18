"""
QUESTION:
Read problems statements in [Hindi], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Dr.D got so famous thanks to his first problem that he decided to commemorate it by making yet another problem with an almost identical statement — he only changed one word.

We want to choose exactly two integers (not necessarily distinct) from the interval $[L, R]$. Find the maximum possible value of the bitwise OR of the chosen integers.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains two space-separated integers $L$, $R$.

------  Output ------
For each test case, print a single line containing one integer — the maximum bitwise OR.

------  Constraints ------
$1 ≤ T ≤ 10^{5}$
$0 ≤ L ≤ R ≤ 10^{18}$

----- Sample Input 1 ------ 
4
1 3
4 5
1031 93714
1000000000123 1000000123456
----- Sample Output 1 ------ 
3
5
131071
1000000192511
"""

def max_bitwise_or(L: int, R: int) -> int:
    """
    Calculate the maximum possible value of the bitwise OR of two integers chosen from the interval [L, R].

    Parameters:
    L (int): The lower bound of the interval.
    R (int): The upper bound of the interval.

    Returns:
    int: The maximum bitwise OR value.
    """
    b1, b2 = bin(L)[2:], bin(R)[2:]
    
    if len(b1) != len(b2):
        max_len = max(len(b1), len(b2))
        return int('1' * max_len, 2)
    else:
        c = 0
        while c < len(b1) and b1[c] == b2[c]:
            c += 1
        ans = b1[:c] + '1' * (len(b1) - c)
        return int(ans, 2)