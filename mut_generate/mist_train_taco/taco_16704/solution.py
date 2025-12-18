"""
QUESTION:
Prime numbers are widely applied for cryptographic and communication technology. A twin prime is a prime number that differs from another prime number by 2. For example, (5, 7) and (11, 13) are twin prime pairs.

In this problem, we call the greater number of a twin prime "size of the twin prime."

Your task is to create a program which reads an integer n and prints a twin prime which has the maximum size among twin primes less than or equals to n

You may assume that 5 ≤ n ≤ 10000.



Input

The input is a sequence of datasets. The end of the input is indicated by a line containing one zero. Each dataset is formatted as follows:


n (integer)


Output

For each dataset, print the twin prime p and q (p < q). p and q should be separated by a single space.

Example

Input

12
100
200
300
0


Output

5 7
71 73
197 199
281 283
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_twin_prime(n):
    for i in range(n, 1, -1):
        if is_prime(i) and is_prime(i - 2):
            return (i - 2, i)
    return None  # In case no twin primes are found, though the problem guarantees there will be.