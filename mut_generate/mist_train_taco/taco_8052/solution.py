"""
QUESTION:
In the year 4242, the language Haskell has evolved so much that it has become an AI. It can solve very challenging problems, in very little time. Humanity is worried that Haskell will take over the world. All hopes remain tied to the Competitive Programming community as they are the expert in shaving milliseconds off code runtime. Haskell creators have found one particular task that if solved faster than Haskell itself, can be used to hack into Haskell's codebase and thus defeat it. The exact details of the task are as follows,


" Calculate the sum, S(N, K) = , for Q queries. Here Fi is ith Fibonacci number defined as: Fi = i if i = 0 or 1 and Fi = Fi-1 + Fi-2 if i >= 2. "


You being a member of the Competitive Programming community are encouraged to make a submission to this task.

-----Input-----

The first line contains a single integer Q, the number of queries.

Each of the next Q lines contain two integers each, Ni and Ki.

-----Output-----

Output Q lines with one integer each. The ith line should contain the value S(Ni, Ki).

-----Constraints-----
- 1 <= Q <= 5*104
- 1 <= N <= 1018
- 1 <= K <= 1018

-----Example-----
Input:
1
1 1
Output:
1
"""

def calculate_sum_of_fibonacci_queries(Q, queries):
    """
    Calculate the sum S(N, K) for Q queries, where S(N, K) is defined as the sum of the ith Fibonacci number multiplied by K raised to the power of i, for i from 0 to N.

    Parameters:
    Q (int): The number of queries.
    queries (list of tuples): A list of tuples where each tuple contains two integers (Ni, Ki).

    Returns:
    list of int: A list of integers where each integer is the result of the calculation for each query.
    """
    mod = 10**9 + 7

    def fibonacci(n):
        if n < 0:
            raise ValueError('Negative arguments not implemented')
        return (_fib(n)[0] % mod + mod) % mod

    def _fib(n):
        if n == 0:
            return (0, 1)
        else:
            (a, b) = _fib(n // 2)
            c = a * (b * 2 - a) % mod
            d = (a * a + b * b) % mod
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    def inv(n):
        return pow(n, mod - 2, mod)

    def ans(n, k):
        k %= mod
        a = pow(k, n + 1, mod)
        b = a * k % mod
        x = a * fibonacci(n + 1) + b * fibonacci(n) - k
        y = inv((k * k + k - 1) % mod)
        return (x * y % mod + mod) % mod

    results = []
    for (n, k) in queries:
        results.append(ans(n, k))
    
    return results