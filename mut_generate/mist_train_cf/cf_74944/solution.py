"""
QUESTION:
Create a function named `fizz_buzz` that takes three arguments: `start`, `end`, and `reverse`. The function should return a list of numbers from `start` to `end` (inclusive) with some numbers replaced by specific strings. The replacement rules are: if a number is divisible by 3 and 5, replace it with 'FizzBuzz'; if a number is divisible by 3, replace it with 'Fizz'; if a number is divisible by 5, replace it with 'Buzz'. The `reverse` argument is a boolean that determines whether the resulting list should be reversed before returning it.
"""

def entrance(start, end, reverse):
    res = []
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('FizzBuzz')
        elif i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    if reverse:
        return res[::-1]
    return res