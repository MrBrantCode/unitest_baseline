"""
QUESTION:
Write a function called `five_nine_twelve` that takes an integer `n` as input and returns the cumulative count of integers less than `n` that meet the following conditions: 
- The number contains the digit 5.
- The number is divisible by either 9 or 12.
- The sum of the digits of the number is divisible by 3.
"""

def five_nine_twelve(n: int) -> int:
    def is_divisible_by_nine_or_twelve(x: int) -> bool:
        return x % 9 == 0 or x % 12 == 0
    
    def sum_of_digits_is_divisible_by_three(x: int) -> bool:
        total = sum(map(int,str(x)))
        return total % 3 == 0

    def number_contains_five(x: int) -> bool:
        return '5' in str(x)
        
    count = 0

    for i in range(n):
        if is_divisible_by_nine_or_twelve(i) and sum_of_digits_is_divisible_by_three(i) and number_contains_five(i):
            count += 1

    return count