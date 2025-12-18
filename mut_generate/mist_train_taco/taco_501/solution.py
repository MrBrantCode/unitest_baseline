"""
QUESTION:
You will be given two integers $a,b$. You are required to output the result of $2^{(2^a)}$ mod $\boldsymbol{b}$.

Constraints

$1\leq a,b\leq10^6$

Input Format

First and only line of the input will contain two integers $a,b$ separated by a single blank space.

Output Format

Output the desired result in a single line.

Sample Input
2 7

Sample Output
2

Explanation

$2^a=4$, $2^{4}=16$, and $\mbox{16}$ mod $7$ is $2$.
"""

def compute_power_mod(a: int, b: int) -> int:
    return pow(2, 2 ** a, b)