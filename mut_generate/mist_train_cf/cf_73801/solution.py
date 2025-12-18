"""
QUESTION:
Write a function `fibber(n, m, p)` that calculates the `n`-th number in the Fibber series, which is a variation of the Fibonacci sequence. The function should use dynamic programming to efficiently calculate the result. The series is defined as follows: `fibber(0, m, p) == 0`, `fibber(1, m, p) == 0`, `fibber(2, m, p) == 1`, and `fibber(n, m, p) == fibber(n-1, m, p) + fibber(n-2, m, p) + fibber(n-3, m, p) - fibber(n-m, p) + 3*fibber(n-p, p)` for `m <= n`, `m > 2`, and `p < m`.
"""

def fibber(n, m, p, fibber_dict={0:0, 1:0, 2:1}):
    if n in fibber_dict: 
        return fibber_dict[n]
    else:
        if m <= n and m > 2 and p < m:
            fibber_dict[n] = fibber(n - 1, m, p, fibber_dict) + fibber(n - 2, m, p, fibber_dict) + fibber(n - 3, m, p, fibber_dict) - fibber(n - m, m, p, fibber_dict) + 3*fibber(n - p, m, p, fibber_dict)
        else:
            fibber_dict[n] = fibber(n - 1, m, p, fibber_dict) + fibber(n - 2, m, p, fibber_dict) + fibber(n - 3, m, p, fibber_dict)
        return fibber_dict[n]