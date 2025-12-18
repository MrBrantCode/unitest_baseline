"""
QUESTION:
Create a function `fizzBuzz` that takes a single parameter `n` (1 <= n <= 100) and returns an array of strings representing the FizzBuzz game output from 1 to `n`, where multiples of three are replaced with "Fizz", multiples of five are replaced with "Buzz", and multiples of both three and five are replaced with "FizzBuzz".
"""

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result