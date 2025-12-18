"""
QUESTION:
A prime number is a natural number which has exactly two distinct natural number divisors: 1 and itself. For example, the first four prime numbers are: 2, 3, 5 and 7.

Write a program which reads a list of N integers and prints the number of prime numbers in the list.

Constraints

1 ≤ N ≤ 10000

2 ≤ an element of the list ≤ 108

Input

The first line contains an integer N, the number of elements in the list.

N numbers are given in the following lines.

Output

Print the number of prime numbers in the given list.

Examples

Input

5
2
3
4
5
6


Output

3


Input

11
7
8
9
10
11
12
13
14
15
16
17


Output

4
"""

import math

def count_primes_in_list(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                return False
        return True
    
    count = 0
    for number in numbers:
        if is_prime(number):
            count += 1
    return count