"""
QUESTION:
Create a function called `five_nine_twelve(n)` that takes an integer `n` as input and returns the count of integers less than `n` that have the digit 5, are divisible by either 9 or 12, and have a digit sum divisible by 3. The function should iterate through all integers less than `n` and return the total count of integers that satisfy these conditions.
"""

def five_nine_twelve(n: int) -> int:
    count = 0
    for num in range(n):
        if '5' in str(num) and (num % 9 == 0 or num % 12 == 0) and sum(int(dig) for dig in str(num)) % 3 == 0:
            count += 1
    return count