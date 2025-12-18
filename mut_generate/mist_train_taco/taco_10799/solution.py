"""
QUESTION:
Calvin has a math assignment at school where he has to evaluate a lot of expressions. Calvin decides to not to waste much of his time. There are ${M}$ expressions overall. By looking at Susie’s answers, Calvin has figured that the answers to all questions form a non decreasing sequence. 

He decides that all his answers are going to be between ${1}$ and $N$ (inclusive). He fills his answer sheet with a random non-decreasing sequence of length ${M}$ where each element is between ${1}$ and $N$. 

Here is the part where the real problem starts for Calvin. He does not want to choose a large value of $N$, because, he will have a lot of options to choose from. Also, if he chooses a very small value of $N$, a lot of answers would become equal and the teacher will become suspicious.  

If $x=\text{max}_{1\leq i\leq N}(f(i))$, f(i) being the frequency or number of times ${i}$ occurs in the sequence of ${M}$ values he picked. Calvin wants to find out expected value of $\boldsymbol{x}$. Help him solve the problem.  

For example, if $M=3$ & $N=3$, the possible sequences are:  

1 1 1 (x = 3)  
1 1 2 (x = 2)  
1 1 3 (x = 2)  
1 2 2 (x = 2)  
1 2 3 (x = 1)  
1 3 3 (x = 2)  
2 2 2 (x = 3)  
2 2 3 (x = 2)  
2 3 3 (x = 2)  
3 3 3 (x = 3)  

expected value of $x=2.2$

Input Format 

The first line contains an integer ${T}$ which refers to the number of test cases. ${T}$ lines follow, each containing $2$ numbers, ${M}$ and $N$ for the corresponding test cases.  

Constraints 

$1\leq T\leq15$ 

$1\leq M\leq250$ 

$1\leq N\leq10^9$  

Output Format 

Output ${T}$ lines, each containing answer to the corresponding test case. Error of upto $10^{-3}$ is allowed.  

Sample Input  

4
1 5
3 3
2 9
9 6

Sample Output  

1.0000000000
2.2000000000
1.2000000000
4.3146853147

Explanation 

For second testcase we have  

$\begin{aligned}
&\text{Seq}\quad\text{Freq} \\
& 111\quad 3  \\
&112\quad2 \\
&113\quad 2 \\
&122\quad 2 \\
&123\quad1\\
&133\quad 2 \\
&222\quad3 \\
&223\quad2 \\
&233\quad 2 \\
&333\quad 3
\end{aligned}$


$\begin{aligned}E(x)&=\sum P_x\times x\\ &=P_1+2P_2+3P_3\\ &=\frac{1}{10}+\frac{2\times6}{10}+\frac{3\times3}{10}\\ &=\frac{22}{10}\end{aligned}$
"""

def calculate_expected_value(M: int, N: int) -> float:
    """
    Calculate the expected value of x for a given M and N.

    Parameters:
    M (int): The length of the non-decreasing sequence.
    N (int): The maximum value in the sequence (values range from 1 to N).

    Returns:
    float: The expected value of x, with an error tolerance of up to 10^-3.
    """
    from decimal import Decimal
    from functools import lru_cache
    from operator import mul
    from functools import reduce

    @lru_cache(maxsize=10 ** 5)
    def binom(n, k):
        if n - k < k:
            k = n - k
        if k < 0:
            return 0
        return reduce(mul, range(n - k + 1, n + 1), 1) // reduce(mul, range(1, k + 1), 1)

    @lru_cache(maxsize=10 ** 5)
    def f(x, M, N):
        return sum((binom(N, k) * (-1) ** k * binom(N + M - k * x - 1, M - k * x) for k in range(M + 1)))

    def solve(M, N):
        r = sum((x * (f(x + 1, M, N) - f(x, M, N)) for x in range(M + 1)))
        r /= f(M + 1, M, N)
        return r

    def f2(x, M, N):
        if x == 0:
            return 0
        s = Decimal(1)
        q = Decimal(1)
        for k in range(min(M // x, N)):
            q *= Decimal(-(N - k)) / Decimal(k + 1)
            for j in range(x):
                q *= Decimal(M - k * x - j) / Decimal(N + M - k * x - 1 - j)
            s += q
        return float(s)

    def solve2(M, N):
        bot = 0
        r = 0
        for x in range(1, M + 1):
            top = f2(x + 1, M, N)
            r += x * (top - bot)
            bot = top
        return r

    return solve2(M, N)