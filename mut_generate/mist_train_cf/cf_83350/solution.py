"""
QUESTION:
Create a function named `sum_multiples_3_5` that takes a list of numbers as input and returns a list of sums. Each sum in the output list is the total of all multiples of 3 and 5 below the corresponding input number.
"""

def sum_multiples_3_5(lst):
    out = []
    for n in lst:
        total_sum = 0
        for i in range(n):
            if i % 3 == 0 or i % 5 == 0:
                total_sum += i
        out.append(total_sum)
    return out