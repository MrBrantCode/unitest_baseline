"""
QUESTION:
Create a function `heptagonal_sequence` that calculates the nth term in the heptagonal sequence, generates the complete sequence up to the nth term, computes the cumulative sum and the product of all terms in the heptagonal sequence up to the nth term, and effectively manages multiple queries. The function should handle scenarios where the input is not a positive integer, surpasses 2000, or is a decimal number necessitating rounding to the nearest integer. 

The function should be able to handle a numerical range, an array of numbers, or an array of ranges, and produce the corresponding sequence of terms. It should also be able to handle incorrect inputs and provide meaningful error messages, and should be capable of managing large inputs effectively without triggering a stack overflow error. The function should utilize dynamic programming and recursion.
"""

def heptagonal_sequence(n):
    if type(n) != int or n < 1 or n > 2000:
        return -1
    else:
        sequence, total_sum, product = [], 0, 1
        for i in range(1, n + 1):
            heptagonal_number = i * (5 * i - 3) // 2
            sequence.append(heptagonal_number)
            total_sum += heptagonal_number
            product *= heptagonal_number
        return sequence, total_sum, product