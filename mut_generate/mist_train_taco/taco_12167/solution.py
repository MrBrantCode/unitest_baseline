"""
QUESTION:
A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)
1^(3) + 5^(3) + 3^(3) = 153

Write a method is_narcissistic(i) (in Haskell: isNarcissistic :: Integer -> Bool) which returns whether or not i is a Narcissistic Number.
"""

def is_narcissistic(n: int) -> bool:
    num = str(n)
    length = len(num)
    return sum((int(a) ** length for a in num)) == n