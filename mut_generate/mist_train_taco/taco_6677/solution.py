"""
QUESTION:
One day Chef was playing with numbers. He loves Lowest Common Multiple (LCM) too much and he is a very curious guy. He always try to do new things. Now he want to make a large number with it. But he doesn't want to take too many numbers.

He is willing to take only three numbers less than or equal to N (not necessarily distinct ) and from those three number he want get the maximum number by taking LCM of the numbers.

As he is busy in playing some more tricks of maths, he assign this task to you.

-----Input-----
First line of input contains an integer t ( t<=1000 ), Number of test cases.

t line follows an integer N

-----Output-----
Print t lines contains a single integer — the maximum possible LCM of three not necessarily distinct positive integers that are not greater than N.

-----Constraints-----
1<= N <= 10^6

-----Example-----
Input:
2
9
7

Output:
504
210


-----Explanation-----
Example case 2. For the last example, we can chose numbers 7, 6, 5 and the LCM of them is 7•6•5 = 210. It is the maximum value we can get.
"""

from math import gcd

def max_lcm_of_three_numbers(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    else:
        c = n * (n - 1)
        k = n - 2
        while True:
            if gcd(k, n - 1) == 1 and gcd(k, n) == 1:
                break
            k -= 1
        d = (n - 1) * (n - 2)
        k1 = n - 3
        while True:
            if gcd(k1, n - 1) == 1 and gcd(k1, n - 2) == 1:
                break
            k1 -= 1
        return max(c * k, d * k1)