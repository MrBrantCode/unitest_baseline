"""
QUESTION:
Write a function named `calculate_average` that calculates the average of a given list of numbers. The function should count duplicate numbers individually and round the average to the nearest integer. It should not use any built-in functions or libraries for mathematical calculations. The function must achieve a time complexity of O(n), where n is the length of the list.
"""

def calculate_average(lst):
    total = 0
    count = 0
    
    for num in lst:
        total += num
        count += 1
    
    average = total / count
    
    decimal_part = average - int(average)
    
    if decimal_part < 0.5:
        rounded_average = int(average)
    else:
        rounded_average = int(average) + 1
    
    return rounded_average