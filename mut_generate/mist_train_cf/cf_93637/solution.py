"""
QUESTION:
Create a function named `calculate_sum` that takes a list of integers as input. The function should return the sum of all even elements in the list only if the list contains more even elements than odd elements and the sum of the even elements is greater than 100. Otherwise, the function should return "No sum found". The input list should contain at least 10 elements, and each element should be a positive integer less than or equal to 100.
"""

def calculate_sum(lst):
    even_sum = 0
    odd_count = 0
    even_count = 0
    
    for num in lst:
        if num % 2 == 0:
            even_sum += num
            even_count += 1
        else:
            odd_count += 1
    
    if even_count > odd_count and even_sum > 100:
        return even_sum
    else:
        return "No sum found"