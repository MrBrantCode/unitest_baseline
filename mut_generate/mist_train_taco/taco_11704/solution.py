"""
QUESTION:
You are given three positive integers $a$, $b$, $c$ ($a < b < c$). You have to find three positive integers $x$, $y$, $z$ such that:

$$x mod y = a,$$ $$y mod z = b,$$ $$z mod x = c.$$

Here $p mod q$ denotes the remainder from dividing $p$ by $q$. It is possible to show that for such constraints the answer always exists.


-----Input-----

The input consists of multiple test cases. The first line contains a single integer $t$ ($1 \le t \le 10000$) — the number of test cases. Description of the test cases follows.

Each test case contains a single line with three integers $a$, $b$, $c$ ($1 \le a < b < c \le 10^8$).


-----Output-----

For each test case output three positive integers $x$, $y$, $z$ ($1 \le x, y, z \le 10^{18}$) such that $x mod y = a$, $y mod z = b$, $z mod x = c$.

You can output any correct answer.


-----Examples-----

Input
4
1 3 4
127 234 421
2 7 8
59 94 388
Output
12 11 4
1063 234 1484
25 23 8
2221 94 2609


-----Note-----

In the first test case:

$$x mod y = 12 mod 11 = 1;$$

$$y mod z = 11 mod 4 = 3;$$

$$z mod x = 4 mod 12 = 4.$$
"""

def find_xyz(a: int, b: int, c: int) -> tuple:
    x = a + b + c
    y = b + c
    z = c
    return (x, y, z)