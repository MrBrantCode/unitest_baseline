"""
QUESTION:
Create a function `calculate_sum` that takes a list of at least 10 positive integers (each less than or equal to 100) as input. The function should return the sum of all even elements in the list if the list contains more even elements than odd elements and the sum is greater than 100. Otherwise, it should return "No sum found".
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