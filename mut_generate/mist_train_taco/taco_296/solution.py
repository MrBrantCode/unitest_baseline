"""
QUESTION:
PROBLEM SPECIFICATION:
You are given three positive integers 'n' , 'a'  and 'b' . In the given range from 1 to 'n' how many distinct numbers are completely divisible by
'a' or 'b' or both?
NOTE: The range includes both 1 and 'n'.

INPUT SPECIFICATION:
You will be given 't' test cases. Each test case will contain three integers 'n' 'a' and 'b'.

OUTPUT SPECIFICATION:
In a single line print the count of numbers that are divisible by 'a' and 'b'.

CONSTRAINTS:
0<t<100
n<10^15
0 ≤ a<10^6
0 ≤ b<10^6

NOTE: In case,if  'a' or 'b' or both of them are zero,print '-1'   (without quotes).

SAMPLE INPUT
1
24 5 3

SAMPLE OUTPUT
11

Explanation

Here in the given range there are total 11 distinct numbers that are divisible by 5 or 3 or both.
"""

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm_value = greater
            break
        greater += 1
    return lcm_value

def count_divisibles_in_range(n, a, b):
    if a == 0 or b == 0:
        return -1
    count = (n // a) + (n // b) - (n // lcm(a, b))
    return count