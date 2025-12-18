"""
QUESTION:
Create a function named `fib` that takes an integer `n` and returns a list of even numbers in the Fibonacci sequence up to `n`. The function should generate the Fibonacci sequence until the sum of the last two numbers exceeds `n`, then filter out the even numbers from the sequence.
"""

def fib(n: int):
    nums = [0, 1]
    while nums[-1] + nums[-2] < n:
        nums.append(nums[-1] + nums[-2])
    return [num for num in nums if num % 2 == 0]