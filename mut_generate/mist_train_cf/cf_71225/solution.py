"""
QUESTION:
Create a function named `sum_nineteen_seventeen_seq` that takes an integer `m` as input. The function should calculate the cumulative sum of numbers less than `m` that end with the digit 9 and are divisible by either 17 or 19.
"""

def sum_nineteen_seventeen_seq(m: int):
    seq = []    
    for i in range(m):
        if str(i)[-1] == '9' and (i % 17 == 0 or i % 19 == 0):
            seq.append(i)
    return sum(seq)