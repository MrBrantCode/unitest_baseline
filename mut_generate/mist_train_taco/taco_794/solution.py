"""
QUESTION:
The events have started and one of them is Void fnx, the most anticipated Coding Event of the college. This year, one question has been bugging the coders for hours, Help them solve it. It goes as follows:

The palindromic number 595 can be written as the sum of consecutive squares: from 6 to 12.

Find the sum of all the numbers between a and b (both inclusive) that are both palindromic and can be written as the sum of consecutive squares.

Input: Two numbers a and b.

Output: A single number which is the answer to the question.

Constraints: 1 ≤ a < b ≤ 100000000

SAMPLE INPUT
1 10

SAMPLE OUTPUT
5

Explanation

There is only one such number between 1 and 10 which can be written as the sum of consecutive squares i.e. 11 + 22 = 5.
"""

from math import sqrt

def palindrome(s):
    return s[::-1] == s

def sum_palindromic_consecutive_squares(a, b):
    def f(N):
        seen = set()
        sqrtN = int(sqrt(N))
        for i in range(1, sqrtN):
            s = i * i
            for j in range(i + 1, sqrtN):
                s += j * j
                if s > N:
                    break
                if palindrome(str(s)):
                    seen.add(s)
        return sum(seen)
    
    return f(b) - f(a - 1)