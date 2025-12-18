"""
QUESTION:
Even if it's a really easy question, she won't be able to answer it

— Perfect Memento in Strict Sense

Cirno's perfect bitmasks classroom has just started!

Cirno gave her students a positive integer $x$. As an assignment, her students need to find the minimum positive integer $y$, which satisfies the following two conditions:

$$x\ {and}\ y > 0$$ $$x\ {xor}\ y > 0$$

Where ${and}$ is the bitwise AND operation , and ${xor}$ is the bitwise XOR operation .

Among the students was Mystia, who was truly baffled by all these new operators. Please help her!


-----Input-----

The first line of input contains a single integer $t$ ($1 \leq t \leq 10^3$) — the number of input test cases.

For each test case, the only line of input contains one integer $x$ ($1 \leq x \leq 2^{30}$).


-----Output-----

For each test case, print a single integer — the minimum number of $y$.


-----Examples-----

Input
7
1
2
5
9
16
114514
1000000
Output
3
3
1
1
17
2
64


-----Note-----

Test case 1:

$1\; {and}\; 3=1>0$, $1\; {xor}\; 3=2>0$.

Test case 2:

$2\; {and}\; 3=2>0$, $2\; {xor}\; 3=1>0$.
"""

def find_min_y(x: int) -> int:
    if x == 1:
        return 3
    else:
        y = x & -x
        if y == x:
            return x + 1
        else:
            return y