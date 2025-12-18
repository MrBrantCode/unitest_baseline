"""
QUESTION:
Create a function called `fib` that takes an integer `n` as input and returns a tuple containing a list of even numbers in the Fibonacci sequence up to `n` and their sum. The Fibonacci sequence should be generated until the last number is less than `n`, not until the length is less than `n`.
"""

def fib(n: int):
    """Return only the even numbers in the Fibonacci sequence up to 'n' and their sum."""
    # Initialize the sequence with the first two Fibonacci numbers.
    nums = [0, 1]
    # Generate the Fibonacci sequence up to 'n'.
    while nums[-1] < n: 
        nums.append(nums[-1] + nums[-2]) 
    # Filter out the even numbers.
    evens = [num for num in nums if num % 2 == 0]
    # Return the even numbers and their sum.
    return evens, sum(evens)