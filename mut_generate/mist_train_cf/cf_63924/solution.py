"""
QUESTION:
Write a function `lucas_sequence(n)` that generates the first `n` numbers in a Lucas sequence. A Lucas sequence starts with 2 and 1, and each subsequent number is the sum of the previous two.
"""

def lucas_sequence(n):
    if n == 0:
        return []
    if n == 1:
        return [2]
    # create the initial list with 2 and 1
    lucas_numbers = [2, 1]
    for i in range(2, n):
        # add the sum of the prior two numbers
        lucas_numbers.append(lucas_numbers[i-1] + lucas_numbers[i-2])
    return lucas_numbers