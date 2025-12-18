"""
QUESTION:
Read problems statements in Russian here 
The Head Chef has been playing with Fibonacci numbers for long . He has learnt several tricks related to Fibonacci numbers . Now he wants to test his chefs in the skills . 
 
A fibonacci number is defined by the recurrence :
 
f(n) = f(n-1) + f(n-2) for n > 2 
and f(1) = 0 
and f(2) = 1 .  

Given a number  A   , determine if it is a fibonacci number.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The only line of each test case contains a single integer  A  denoting the number to be checked .

------ Output ------ 

For each test case, output a single line containing "YES" if the given number is a fibonacci number , otherwise output a single line containing "NO" . 

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ number of digits in A  ≤ 1000$
$  The sum of number of digits in A in all test cases   ≤ 10000.  $

----- Sample Input 1 ------ 
3
3
4
5
----- Sample Output 1 ------ 
YES
NO
YES
----- explanation 1 ------ 
Example case 1. The first few fibonacci numbers are 0 , 1 , 1 , 2 , 3 ,5 , 8 , 13 and so on and the series is increasing . Only 3 and 5 appear in this series while 4 does not appear in the series .
"""

def is_fibonacci_number(A: int) -> str:
    """
    Determines if the given number A is a Fibonacci number.

    Parameters:
    A (int): The number to be checked.

    Returns:
    str: "YES" if A is a Fibonacci number, otherwise "NO".
    """
    max_fib_length = 1000
    fibs = []

    def fibonacci(n):
        def fib_inner(n):
            if n == 0:
                return (0, 1)
            (u, v) = fib_inner(n >> 1)
            q = (n & 2) - 1
            u *= u
            v *= v
            if n & 1:
                return (u + v, 3 * v - 2 * (u - q))
            return (2 * (v + q) - 3 * u, u + v)
        (u, v) = fib_inner(n >> 1)
        l = 2 * v - u
        if n & 1:
            q = (n & 2) - 1
            return v * l + q
        return u * l

    def gen_fibs():
        n = 1
        f = fibonacci(n)
        while len(str(f)) < max_fib_length:
            fibs.append(f)
            n += 1
            f = fibonacci(n)

    gen_fibs()
    return 'YES' if A in fibs else 'NO'