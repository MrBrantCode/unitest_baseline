"""
QUESTION:
Archith loves to play with number series. Archith asked his girlfriend to a date. But she was busy in solving the homework on triangular series which stated that find the least number which has higher divisors than n in a triangular series. His girlfriend made a condition that if he solves this assignment for her she will come for date. Archith dont want to waste time he is developing a code. Put yourself in the position of archith and solve this problem.(#projecteuler 13)

INPUT:
T test cases
every t lines consists of a number n which specifies the no of divisors.
OUTPUT:
output the least triangular number which has higher no of divisors than n.

1<T<11
1<n<10^2

example:

triangular series will be as follows 1,3,6,10........
if n =2
6 has 4 divisors.So 6 will be the least number to have more than n divisors.

SAMPLE INPUT
4
1
2
3
4

SAMPLE OUTPUT
3
6
6
28
"""

from math import sqrt

def factors(n):
    final = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            final.add(i)
            final.add(n // i)
    return len(final)

def find_least_triangular_number_with_divisors(n):
    diff = 3
    start = 3
    ans = start
    while factors(start) <= n:
        start += diff
        diff += 1
        ans = start
    return ans