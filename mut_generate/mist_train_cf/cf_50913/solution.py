"""
QUESTION:
Write a function named `even_odd_count` that takes an integer `num` as input and returns a tuple of two tuples. The first inner tuple should contain the count of even and odd digits in `num`, and the second inner tuple should contain the sum of even and odd digits in `num`. The function should consider the absolute value of `num` and ignore any non-digit characters.
"""

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    even_sum = 0
    odd_sum = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
            even_sum += int(digit)
        else:
            odd_count += 1
            odd_sum += int(digit)
    return (even_count, odd_count), (even_sum, odd_sum)