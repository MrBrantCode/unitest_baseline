"""
QUESTION:
Implement the `multiply_without_operator` function that takes two integers `num_1` and `num_2` as input and returns their product without using the multiplication operator (*). The function should handle negative numbers and minimize the number of mathematical operations performed. Assume the input numbers will always be integers.
"""

def multiply_without_operator(num_1: int, num_2: int) -> int:
    if num_1 == 0 or num_2 == 0:
        return 0
    
    negative_result = False
    if num_1 < 0:
        num_1 = -num_1
        negative_result = not negative_result
    if num_2 < 0:
        num_2 = -num_2
        negative_result = not negative_result
    
    result = 0
    for _ in range(num_2):
        result += num_1
    
    return -result if negative_result else result