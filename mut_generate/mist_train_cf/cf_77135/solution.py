"""
QUESTION:
Implement a function 'intersperse' that takes a list of integers 'numbers' and an integer 'delimeter' as input. The function should return a list where the integer 'delimeter' is inserted between each pair of consecutive integers in 'numbers'. Additionally, the function should check if the list of 'numbers' supplied is strictly increasing (i.e., each element is greater than the previous one) and return an error message if the list is not strictly increasing. The function should not remove any elements from the input list 'numbers'.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert 'delimeter' between each pair of consecutive elements in 'numbers'. Check if 'numbers' is strictly increasing.
    """
    # Check if numbers is strictly increasing
    if len(numbers) > 1 and not all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1)):
        return "Numbers list is not strictly increasing!"
    
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:        
            result.append(delimeter)        
    return result