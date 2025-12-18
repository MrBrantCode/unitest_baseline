"""
QUESTION:
Write a function `complex_operation_result(a, b, start, operation, base, repeat)` that takes two positive integers `a` and `b` (where `a` is less than or equal to `b`), a `start` number, an `operation` ('+' or '*'), a `base` system integer between 2 and 10 (inclusive), and a `repeat` factor. The function should perform the `operation` on all numbers from `a` through `b` (inclusive) `repeat` times, starting with the `start` number, then convert the result into the `base` system and return it as a string. Return -1 for invalid inputs such as `a` greater than `b`, a negative `start` number, an incorrect `operation`, or an out-of-range `base`.
"""

def complex_operation_result(a, b, start, operation, base, repeat):
    if a > b or start < 0 or operation not in ['+', '*'] or not(2 <= base <= 10):
        return -1

    operations = {'+': lambda x, y: x+y, '*': lambda x, y: x*y}

    for _ in range(repeat):
        for i in range(a, b+1):
            start = operations[operation](start, i)

    if base == 2:
        return bin(start)[2:]
    elif base == 8:
        return oct(start)[2:]
    elif base == 10:
        return str(start)
    else:
        digits = "0123456789"
        result = ""
        while start > 0:
            result = digits[start % base] + result
            start = start // base
        return result