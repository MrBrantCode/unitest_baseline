"""
QUESTION:
We all know the impressive story of Robin Hood. Robin Hood uses his archery skills and his wits to steal the money from rich, and return it to the poor.

There are n citizens in Kekoland, each person has ci coins. Each day, Robin Hood will take exactly 1 coin from the richest person in the city and he will give it to the poorest person (poorest person right after taking richest's 1 coin). In case the choice is not unique, he will select one among them at random. Sadly, Robin Hood is old and want to retire in k days. He decided to spend these last days with helping poor people. 

After taking his money are taken by Robin Hood richest person may become poorest person as well, and it might even happen that Robin Hood will give his money back. For example if all people have same number of coins, then next day they will have same number of coins too. 

Your task is to find the difference between richest and poorest persons wealth after k days. Note that the choosing at random among richest and poorest doesn't affect the answer.

Input

The first line of the input contains two integers n and k (1 ≤ n ≤ 500 000, 0 ≤ k ≤ 109) — the number of citizens in Kekoland and the number of days left till Robin Hood's retirement.

The second line contains n integers, the i-th of them is ci (1 ≤ ci ≤ 109) — initial wealth of the i-th person.

Output

Print a single line containing the difference between richest and poorest peoples wealth.

Examples

Input

4 1
1 1 4 2


Output

2


Input

3 1
2 2 2


Output

0

Note

Lets look at how wealth changes through day in the first sample.

  1. [1, 1, 4, 2]
  2. [2, 1, 3, 2] or [1, 2, 3, 2]



So the answer is 3 - 1 = 2

In second sample wealth will remain the same for each person.
"""

def calculate_wealth_difference(n, k, C):
    C.sort()
    (m, r) = divmod(sum(C), n)
    m1 = m + 1 if r else m
    
    c_lo = C[0]
    k_lo = k
    for (i, c) in enumerate(C):
        if c_lo == m:
            break
        c_m = min(c, m)
        dc = c_m - c_lo
        dk = i * dc
        if k_lo >= dk:
            k_lo -= dk
            c_lo = c_m
        else:
            dc = k_lo // i
            c_lo += dc
            break
    
    c_hi = C[-1]
    k_hi = k
    for (i, c) in enumerate(reversed(C)):
        if c_hi == m1:
            break
        c_m1 = max(c, m1)
        dc = c_hi - c_m1
        dk = i * dc
        if k_hi >= dk:
            k_hi -= dk
            c_hi = c_m1
        else:
            dc = k_hi // i
            c_hi -= dc
            break
    
    return c_hi - c_lo