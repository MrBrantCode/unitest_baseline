"""
QUESTION:
Burenka came to kindergarden. This kindergarten is quite strange, so each kid there receives two fractions ($\frac{a}{b}$ and $\frac{c}{d}$) with integer numerators and denominators. Then children are commanded to play with their fractions.

Burenka is a clever kid, so she noticed that when she claps once, she can multiply numerator or denominator of one of her two fractions by any integer of her choice (but she can't multiply denominators by $0$). Now she wants know the minimal number of claps to make her fractions equal (by value). Please help her and find the required number of claps!


-----Input-----

The first line contains one integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases. Then follow the descriptions of each test case.

The only line of each test case contains four integers $a$, $b$, $c$ and $d$ ($0 \leq a, c \leq 10^9$, $1 \leq b, d \leq 10^9$) — numerators and denominators of the fractions given to Burenka initially.


-----Output-----

For each test case print a single integer — the minimal number of claps Burenka needs to make her fractions equal.


-----Examples-----

Input
8
2 1 1 1
6 3 2 1
1 2 2 3
0 1 0 100
0 1 228 179
100 3 25 6
999999999 300000000 666666666 100000000
33 15 0 84
Output
1
0
2
0
1
1
1
1


-----Note-----

In the first case, Burenka can multiply $c$ by $2$, then the fractions will be equal.

In the second case, fractions are already equal.

In the third case, Burenka can multiply $a$ by $4$, then $b$ by $3$. Then the fractions will be equal ($\frac{1 \cdot 4}{2 \cdot 3} = \frac{2}{3}$).
"""

def minimal_claps_to_equal_fractions(a: int, b: int, c: int, d: int) -> int:
    """
    Calculate the minimal number of claps required to make the fractions (a/b) and (c/d) equal.

    Parameters:
    a (int): Numerator of the first fraction.
    b (int): Denominator of the first fraction.
    c (int): Numerator of the second fraction.
    d (int): Denominator of the second fraction.

    Returns:
    int: The minimal number of claps required.
    """
    x = a * d
    y = b * c
    
    if x == y:
        return 0
    elif x == 0 or y == 0:
        return 1
    elif x % y == 0 or y % x == 0:
        return 1
    else:
        return 2