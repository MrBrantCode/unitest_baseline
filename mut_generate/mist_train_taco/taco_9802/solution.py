"""
QUESTION:
You are given an integer $n$ ($n \ge 0$) represented with $k$ digits in base (radix) $b$. So,

$$n = a_1 \cdot b^{k-1} + a_2 \cdot b^{k-2} + \ldots a_{k-1} \cdot b + a_k.$$

For example, if $b=17, k=3$ and $a=[11, 15, 7]$ then $n=11\cdot17^2+15\cdot17+7=3179+255+7=3441$.

Determine whether $n$ is even or odd.


-----Input-----

The first line contains two integers $b$ and $k$ ($2\le b\le 100$, $1\le k\le 10^5$) — the base of the number and the number of digits.

The second line contains $k$ integers $a_1, a_2, \ldots, a_k$ ($0\le a_i < b$) — the digits of $n$.

The representation of $n$ contains no unnecessary leading zero. That is, $a_1$ can be equal to $0$ only if $k = 1$.


-----Output-----

Print "even" if $n$ is even, otherwise print "odd".

You can print each letter in any case (upper or lower).


-----Examples-----
Input
13 3
3 2 7

Output
even

Input
10 9
1 2 3 4 5 6 7 8 9

Output
odd

Input
99 5
32 92 85 74 4

Output
odd

Input
2 2
1 0

Output
even



-----Note-----

In the first example, $n = 3 \cdot 13^2 + 2 \cdot 13 + 7 = 540$, which is even.

In the second example, $n = 123456789$ is odd.

In the third example, $n = 32 \cdot 99^4 + 92 \cdot 99^3 + 85 \cdot 99^2 + 74 \cdot 99 + 4 = 3164015155$ is odd.

In the fourth example $n = 2$.
"""

def determine_even_or_odd(b: int, k: int, a: list) -> str:
    """
    Determines whether the number n, represented by k digits in base b, is even or odd.

    Parameters:
    b (int): The base of the number (2 <= b <= 100).
    k (int): The number of digits (1 <= k <= 10^5).
    a (list): A list of integers representing the digits of n (0 <= a_i < b).

    Returns:
    str: "even" if n is even, otherwise "odd".
    """
    if b % 2 == 0:
        a = a[-1:]
    return 'even' if sum(a) % 2 == 0 else 'odd'