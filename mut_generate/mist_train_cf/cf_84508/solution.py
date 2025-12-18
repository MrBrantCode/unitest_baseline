"""
QUESTION:
Create a function called `collatz` that takes a positive integer `n` as input and returns a tuple containing the Collatz sequence starting from `n` up to 1 and the number of steps taken to reach 1. Implement memoization to store previously computed sequences and recall them when needed to avoid redundant calculations. Additionally, create a function called `multiple_collatz` that takes a list of positive integers as input and returns a list of tuples, where each tuple contains the Collatz sequence and the number of steps for each input number.
"""

def collatz(n):
    collatz_dict = {1: ([1], 0)}
    if n not in collatz_dict:
        if n % 2 == 0:
            sequence, steps = collatz(n//2)
            collatz_dict[n] = ([n] + sequence, steps + 1)
        else:
            sequence, steps = collatz(3*n + 1)
            collatz_dict[n] = ([n] + sequence, steps + 1)
    return collatz_dict[n]

def multiple_collatz(nums):
    return [collatz(n) for n in nums]