"""
QUESTION:
Write a recursive function called `calculate_sum` that calculates the sum of a list of numbers. The function should exclude numbers that are divisible by 3 or 5, but include numbers that are divisible by both 3 and 5. If the sum exceeds 1000, the function should return the sum divided by 2. The function should take the list of numbers and an optional index and current sum as parameters, defaulting to 0 for the index and current sum.
"""

def calculate_sum(numbers, index=0, current_sum=0):
    if current_sum >= 1000:
        return current_sum / 2
    
    if index >= len(numbers):
        return current_sum
    
    if (numbers[index] % 3 == 0 and numbers[index] % 5 == 0) or (numbers[index] % 3 != 0 and numbers[index] % 5 != 0):
        current_sum += numbers[index]
    
    return calculate_sum(numbers, index+1, current_sum)