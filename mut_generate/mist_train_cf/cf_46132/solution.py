"""
QUESTION:
Define the function $T_5(n)$ as the count of integers $i$ that fulfill the condition $f_5((2 \cdot i - 1)!) < 2 \cdot f_5(i!)$ within the range $1 \le i \le n$, where $f_5(n)$ is the greatest integer $x$ such that $5^x$ is a divisor of $n$. Write a function `T_5(n)` to calculate $T_5(n)$ where n is a positive integer. The function should be efficient enough to compute $T_5(10^{18})$ in a reasonable amount of time.
"""

def T_5(n):
    result = 0
    div = 5
    while div <= n:
      result += n//div - n//(div*5)
      div *= 5
    return result