"""
QUESTION:
Recall the definition of the Fibonacci numbers:


f1 := 1

f2 := 2

fn := fn-1 + fn-2 (n>=3)

Given two numbers a and b, calculate how many Fibonacci numbers are in the range [a,b].


-----Input-----

The input contains several test cases. Each test case consists of two non-negative integer numbers a and b. Input is terminated by a=b=0. Otherwise, a<=b<=10^100. The numbers a and b are given with no superfluous leading zeros.

-----Output-----

For each test case output on a single line the number of Fibonacci numbers fi with a<=fi<=b.

-----Example-----
Input:

10 100
1234567890 9876543210
0 0

Output:

5
4
"""

def count_fibonacci_in_range(a: int, b: int) -> int:
    """
    Counts the number of Fibonacci numbers within the range [a, b].

    Parameters:
    a (int): The lower bound of the range (inclusive).
    b (int): The upper bound of the range (inclusive).

    Returns:
    int: The number of Fibonacci numbers in the range [a, b].
    """
    # Precompute Fibonacci numbers up to a reasonable limit
    F = [1, 1]
    for i in range(500):
        F.append(F[-2] + F[-1])
    
    # Filter Fibonacci numbers within the range [a, b]
    fib_in_range = [x for x in F if a <= x <= b]
    
    # Return the count of Fibonacci numbers in the range
    return len(fib_in_range)