"""
QUESTION:
Create a function called `calculate_sum` that takes a list of numbers as input and returns their sum, excluding numbers that are divisible by 3 or 5, but including numbers that are divisible by both 3 and 5. The function must use recursion and stop when the sum reaches or exceeds 1000, at which point it returns the sum divided by 2.
"""

def calculate_sum(numbers, index=0, current_sum=0):
    if current_sum >= 1000:
        return current_sum / 2
    
    if index >= len(numbers):
        return current_sum
    
    if numbers[index] % 3 == 0 and numbers[index] % 5 == 0:
        current_sum += numbers[index]
    
    if numbers[index] % 3 != 0 and numbers[index] % 5 != 0:
        current_sum += numbers[index]
    
    return calculate_sum(numbers, index+1, current_sum)