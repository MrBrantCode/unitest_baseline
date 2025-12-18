"""
QUESTION:
Not so long ago, Vlad came up with an interesting function:

$f_a(x)=\left\lfloor\frac{x}{a}\right\rfloor + x mod a$, where $\left\lfloor\frac{x}{a}\right\rfloor$ is $\frac{x}{a}$, rounded down, $x mod a$ — the remainder of the integer division of $x$ by $a$.

For example, with $a=3$ and $x=11$, the value $f_3(11) = \left\lfloor\frac{11}{3}\right\rfloor + 11 mod 3 = 3 + 2 = 5$.

The number $a$ is fixed and known to Vlad. Help Vlad find the maximum value of $f_a(x)$ if $x$ can take any integer value from $l$ to $r$ inclusive ($l \le x \le r$).


-----Input-----

The first line of input data contains an integer $t$ ($1 \le t \le 10^4$) — the number of input test cases.

This is followed by $t$ lines, each of which contains three integers $l_i$, $r_i$ and $a_i$ ($1 \le l_i \le r_i \le 10^9, 1 \le a_i \le 10^9$) — the left and right boundaries of the segment and the fixed value of $a$.


-----Output-----

For each test case, output one number on a separate line — the maximum value of the function on a given segment for a given $a$.


-----Examples-----

Input
5
1 4 3
5 8 4
6 10 6
1 1000000000 1000000000
10 12 8
Output
2
4
5
999999999
5


-----Note-----

In the first sample:

$f_3(1) = \left\lfloor\frac{1}{3}\right\rfloor + 1 mod 3 = 0 + 1 = 1$,

$f_3(2) = \left\lfloor\frac{2}{3}\right\rfloor + 2 mod 3 = 0 + 2 = 2$,

$f_3(3) = \left\lfloor\frac{3}{3}\right\rfloor + 3 mod 3 = 1 + 0 = 1$,

$f_3(4) = \left\lfloor\frac{4}{3}\right\rfloor + 4 mod 3 = 1 + 1 = 2$

As an answer, obviously, $f_3(2)$ and $f_3(4)$ are suitable.
"""

def max_fa_value(l: int, r: int, a: int) -> int:
    """
    Calculate the maximum value of the function f_a(x) = floor(x / a) + x % a
    for x in the range [l, r] inclusive.

    Parameters:
    l (int): The lower bound of the range.
    r (int): The upper bound of the range.
    a (int): The fixed value for the function.

    Returns:
    int: The maximum value of f_a(x) in the range [l, r].
    """
    # Calculate the value at the upper bound
    max_value = r // a + r % a
    
    # Calculate the value just before a multiple of a within the range
    if r - r % a - 1 >= l:
        max_value = max(max_value, (r - r % a - 1) // a + (r - r % a - 1) % a)
    
    return max_value