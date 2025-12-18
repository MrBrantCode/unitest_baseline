"""
QUESTION:
Determine the terminal 5 digits of the aggregate of all integers n, where 10 < n < 10^100, such that n can divide its own right-rotation. In a right-rotation, the terminal digit is transposed to the commencement of the number. For example, the right-rotation of 142857 is 714285. Write a function sum_right_rot_divs(limit) that calculates this aggregate.
"""

def sum_right_rot_divs(limit):
    total = 0
    for d in [2, 5, 7]:
        m = d
        while True:
            n = d + m * 10
            if n >= limit:
                break
            total += n
            m *= 10
            m += d
    return total % 10**5