"""
QUESTION:
There is a strange counter. At the first second, it displays the number $3$. Each second, the number displayed by decrements by $\mbox{1}$ until it reaches $\mbox{1}$. In next second, the timer resets to $2\times\textbf{the initial number for the prior cycle}$ and continues counting down. The diagram below shows the counter values for each time $\boldsymbol{\boldsymbol{t}}$ in the first three cycles:

Find and print the value displayed by the counter at time $\boldsymbol{\boldsymbol{t}}$.  

Function Description  

Complete the strangeCounter function in the editor below.  

strangeCounter has the following parameter(s):  

int t: an integer   

Returns  

int: the value displayed at time $\boldsymbol{\boldsymbol{t}}$  

Input Format

A single integer, the value of $\boldsymbol{\boldsymbol{t}}$.

Constraints

$1\leq t\leq10^{12}$

Subtask

$1\leq t\leq10^5$ for $60\%$ of the maximum score.

Sample Input
4

Sample Output
6

Explanation

Time $t=4$ marks the beginning of the second cycle.  It is double the number displayed at the beginning of the first cycle:$2\times3=6$. This is shown in the diagram in the problem statement.
"""

def strange_counter(t: int) -> int:
    t1 = 3
    while t1 < t:
        t -= t1
        t1 *= 2
    return t1 - t + 1