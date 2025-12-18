"""
QUESTION:
Create a function called `prime_sequence_dict` that takes two integer parameters `start` and `end` and returns a dictionary where the keys are prime numbers within the range from `start` to `end` (exclusive) and the values are the difference between the sum of an arithmetic progression sequence starting from 15 with a common difference of 5 and the sum of a geometric progression sequence starting from 2 with a common ratio of 3, both sequences having a length equal to their corresponding prime number key. The function should use list and dictionary comprehensions and implement the summation without using built-in Python functions (except for the `range` function).
"""

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def generate_sequences(n):
    ap = [15 + 5*i for i in range(n)]
    gp = [2 * 3**i for i in range(n)]
    return ap, gp

def reduce_sequences(ap, gp):
    sum_ap, sum_gp = 0, 0
    for i in ap:
        sum_ap += i
    for i in gp:
        sum_gp += i
    return sum_ap - sum_gp

def prime_sequence_dict(start, end):
    return {i: reduce_sequences(*generate_sequences(i)) for i in range(start, end) if is_prime(i)}