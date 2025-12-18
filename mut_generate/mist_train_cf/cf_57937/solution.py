"""
QUESTION:
Write a function `special_numbers` that takes a non-empty list of positive integers as input. The function should return all unique numbers in the list that satisfy the following conditions:
- The number of its digits is less than or equal to the number itself.
- The number of its digits is a composite number.
- The input list forms a decreasing factorial sequence.

If no such numbers are found, the function should return an empty list.
"""

def special_numbers(array):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    if not array or factorial(len(array) - 1) != array[0]:
        return []
    
    result = []
    array_set = set(array)
    for num in array_set:
        if len(str(num)) <= num and is_composite(len(str(num))):
            result.append(num)
    return result