"""
QUESTION:
Write a function `cumulative_sum(n)` that calculates the cumulative sum of individual digits present within the range of 1 to N (inclusive), where N is a positive integer. The function should return the total sum of all digits.
"""

def entrance(n):
    total_sum = 0
    for i in range(1,n+1):
        for digit in str(i):
            total_sum += int(digit)
    return total_sum