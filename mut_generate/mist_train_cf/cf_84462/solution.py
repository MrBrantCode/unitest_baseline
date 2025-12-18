"""
QUESTION:
Write a function `countNumbersWithUniqueDigits(n)` that takes an integer `n` as input and returns the count of all numbers with non-repeating digits, `x`, where `0 <= x < 10n`. The input `n` is restricted to `0 <= n <= 10`.
"""

def countNumbersWithUniqueDigits(n: int) -> int:
    
    if n == 0: 
        return 1
        
    result = 10
    unique_digits = 9
    available_number = 9
    
    while n > 1 and available_number > 0:
        unique_digits = unique_digits * available_number
        result += unique_digits
        available_number -= 1
        n -= 1
            
    return result