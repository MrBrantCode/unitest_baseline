"""
QUESTION:
This is Fibonacci madness.
Given a number n. Print the first n Fibonacci numbers in reverse order.

Input:

First line is number T denoting number of test cases.
T lines follow. Each line has number N.

Output:

Print the first n Fibonacci numbers in reverse order for all test cases.

Constraints:

1 ≤ T ≤ 10

0 ≤ N ≤ 100

Example

Input:
3

1

7

4
Output:
0

8 5 3 2 1 1 0 

2 1 1 0

SAMPLE INPUT
3
1
7
4

SAMPLE OUTPUT
0 
8 5 3 2 1 1 0 
2 1 1 0
"""

def reverse_fibonacci_sequence(T, N):
    results = []
    
    for n in N:
        if 1 <= n <= 100:
            x, y = 0, 1
            fib_sequence = []
            
            while n >= 1:
                fib_sequence.append(x)
                x, y = y, x + y
                n -= 1
            
            fib_sequence.reverse()
            results.append(fib_sequence)
    
    return results