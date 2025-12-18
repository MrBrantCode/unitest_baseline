"""
QUESTION:
Aniruddha loves to code on HackerEarth. There are some type of problems which he likes the most.
Problems are tagged with non empty strings containing only 'H' or 'E' or both. But he likes the problems tagged with strings containing no consecutive E's. Given an integer N, find maximum number of problems Aniruddha may like which are tagged with strings of length less than or equal to N.

Input
First line contains single integer, T, the number of test cases.  Each of next T lines contains single integer N.

Output
For each test case output single integer, the answer to the problem i.e maximum number of problems Aniruddha may like which are tagged with strings of length less than or equal to N. Output answer modulo 10^9 + 7 (i.e. 1000000007).

Constraints
1 ≤ T ≤ 10^6
1 ≤ N ≤ 10^6

SAMPLE INPUT
2
2
3

SAMPLE OUTPUT
5
10
"""

def calculate_max_liked_problems(N: int) -> int:
    MOD = 1000000007
    
    # Precompute Fibonacci sequence and their sums up to 10^6
    fib = [2, 3]
    sum_fib = [2, 5]
    
    for i in range(1, N):
        next_fib = (fib[i] + fib[i-1]) % MOD
        fib.append(next_fib)
        sum_fib.append((sum_fib[i] + next_fib) % MOD)
    
    # Return the sum of Fibonacci numbers up to N-1
    return sum_fib[N-1]