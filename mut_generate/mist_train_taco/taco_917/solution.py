"""
QUESTION:
You are a teacher at a cram school for elementary school pupils.

One day, you showed your students how to calculate division of fraction in a class of mathematics. Your lesson was kind and fluent, and it seemed everything was going so well - except for one thing. After some experiences, a student Max got so curious about how precise he could compute the quotient. He tried many divisions asking you for a help, and finally found a case where the answer became an infinite fraction. He was fascinated with such a case, so he continued computing the answer. But it was clear for you the answer was an infinite fraction - no matter how many digits he computed, he wouldn’t reach the end.

Since you have many other things to tell in today’s class, you can’t leave this as it is. So you decided to use a computer to calculate the answer in turn of him. Actually you succeeded to persuade him that he was going into a loop, so it was enough for him to know how long he could compute before entering a loop.

Your task now is to write a program which computes where the recurring part starts and the length of the recurring part, for given dividend/divisor pairs. All computation should be done in decimal numbers. If the specified dividend/divisor pair gives a finite fraction, your program should treat the length of the recurring part as 0.



Input

The input consists of multiple datasets. Each line of the input describes a dataset. A dataset consists of two positive integers x and y, which specifies the dividend and the divisor, respectively. You may assume that 1 ≤ x < y ≤ 1,000,000.

The last dataset is followed by a line containing two zeros. This line is not a part of datasets and should not be processed.

Output

For each dataset, your program should output a line containing two integers separated by exactly one blank character.

The former describes the number of digits after the decimal point before the recurring part starts. And the latter describes the length of the recurring part.

Example

Input

1 3
1 6
3 5
2 200
25 99
0 0


Output

0 1
1 1
1 0
2 0
0 2
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f(n, m):
    if m == 1:
        return 0
    x = 1
    for i in range(m):
        x = x * n % m
        if x == 1:
            return i + 1
    return 0

def find_recurring_part(dividend, divisor):
    if dividend == 0 or divisor == 0:
        return 0, 0
    
    # Reduce the fraction to its simplest form
    common_divisor = gcd(dividend, divisor)
    dividend //= common_divisor
    divisor //= common_divisor
    
    # Count the number of digits before the recurring part starts
    cnt = 0
    d = gcd(divisor, 10)
    while d != 1:
        divisor //= d
        cnt += 1
        d = gcd(divisor, 10)
    
    # Find the length of the recurring part
    recurring_length = f(10, divisor)
    
    return cnt, recurring_length