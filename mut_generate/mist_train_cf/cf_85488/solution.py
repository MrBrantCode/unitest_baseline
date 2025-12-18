"""
QUESTION:
Write a function `f(n)` that returns a list of `n` elements where the `i-th` index contains the factorial of `i` if `i` is even, and the cumulative sum of digits from 1 to `i` if `i` is odd. Assume `i` starts from 1. The factorial of `i` is the product of all integers from 1 to `i`, and the cumulative sum is the sum of all integers from 1 to `i`. 

Restrictions: The function should use helper functions to calculate the factorial and cumulative sum.
"""

def factorial(num):
    """ Calculate the factorial of a given number """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def cumulative_sum(num):
    """ Calculate the cumulative sum of numbers from 1 to a given number """
    return sum(range(1, num+1))


def entrance(n):
    resultList = [0] * n
    for i in range(n):
        if (i+1) % 2 == 0:
            resultList[i] = factorial(i+1)
        else:
            resultList[i] = cumulative_sum(i+1)
    return resultList