"""
QUESTION:
To round an integer a, it is customary to round to some multiple of a power of 10, and you will round it accordingly. This time, rules have changed. Given an int n and an int b, round n to the nearest value which is a multiple of b.
 If n is exactly halfway between two multiples of b, print the larger value.

INPUT

First line of input gives T, the number of test cases.
T lines follow, each line contains n and b.

OUTPUT

For every test case, round n to the nearest value which is a multiple of b.

CONSTRAINTS
n will be between 1 and 1000000, inclusive.
b will be between 2 and 500, inclusive.
1 ≤ T ≤ 50

SAMPLE INPUT
2
5 10
100 3

SAMPLE OUTPUT
10
99

Explanation

CASE 1: We round up because 5 is an equal distance between 0 and 10.

CASE 2: 100 is closer to 99 than 102.
"""

def round_to_nearest_multiple(n: int, b: int) -> int:
    # Calculate the two closest multiples of b around n
    lower_multiple = (n // b) * b
    upper_multiple = lower_multiple + b
    
    # Determine which multiple is closer to n
    if abs(n - lower_multiple) < abs(n - upper_multiple):
        return lower_multiple
    elif abs(n - lower_multiple) > abs(n - upper_multiple):
        return upper_multiple
    else:
        # If n is exactly halfway between two multiples, return the larger one
        return upper_multiple