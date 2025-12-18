"""
QUESTION:
Little C loves number «3» very much. He loves all things about it.

Now he has a positive integer $n$. He wants to split $n$ into $3$ positive integers $a,b,c$, such that $a+b+c=n$ and none of the $3$ integers is a multiple of $3$. Help him to find a solution.


-----Input-----

A single line containing one integer $n$ ($3 \leq n \leq 10^9$) — the integer Little C has.


-----Output-----

Print $3$ positive integers $a,b,c$ in a single line, such that $a+b+c=n$ and none of them is a multiple of $3$.

It can be proved that there is at least one solution. If there are multiple solutions, print any of them.


-----Examples-----
Input
3

Output
1 1 1
Input
233
Output
77 77 79
"""

def split_into_three_non_multiples_of_three(n):
    q = n // 3
    r = n % 3
    
    if r == 0:
        if n == 3:
            return (1, 1, 1)
        elif n == 6:
            return (2, 2, 2)
        elif q % 3 == 0:
            return (q - 2, q + 1, q + 1)
        else:
            return (q, q, q)
    elif r == 1:
        if n == 4:
            return (2, 1, 1)
        elif n == 7:
            return (2, 1, 4)
        elif q % 3 == 0:
            return (q + 1, q + 1, q - 1)
        elif q % 3 == 1:
            return (q + 1, q, q)
        else:
            return (q - 1, q + 2, q)
    elif n == 5:
        return (2, 2, 1)
    elif n == 8:
        return (2, 2, 4)
    elif q % 3 == 0:
        return (q + 2, q + 1, q - 1)
    elif q % 3 == 1:
        return (q + 1, q + 1, q)
    else:
        return (q + 2, q, q)