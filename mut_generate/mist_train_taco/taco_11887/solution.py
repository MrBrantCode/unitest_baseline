"""
QUESTION:
Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: **begin**, **end**, **step**.

If **begin** value is greater than the **end**, function should returns **0**

*Examples*

~~~if-not:nasm

~~~

This is the first kata in the series:

1) Sum of a sequence (this kata)  
2) [Sum of a Sequence [Hard-Core Version]](https://www.codewars.com/kata/sum-of-a-sequence-hard-core-version/javascript)
"""

def sum_sequence(begin, end, step):
    if begin > end:
        return 0
    return sum(range(begin, end + 1, step))