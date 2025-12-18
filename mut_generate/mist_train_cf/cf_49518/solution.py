"""
QUESTION:
Write a function called `find_numbers(max_n)` that calculates the aggregate of the positive integers `n` less than or equal to `max_n` for which the number of integers `x` satisfying the conditions `1 < x < n` and `x^3 ≡ 1 mod n` equals `242`. The input `max_n` will be a large integer.
"""

def find_numbers(max_n):
    result = 0
    i = 5
    while True:
        n = 2**i
        if n > max_n:
            break

        if 2*(i-1) % 11 == 0:
            result += n

        i *= 2
    return result