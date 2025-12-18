"""
QUESTION:
Write a function `calculate_average(lst)` that calculates the average of the elements in a given list `lst` and rounds the result to the nearest integer. The function should count duplicates individually and have a time complexity of O(n), where n is the length of the list. Do not use any built-in functions or libraries for mathematical calculations.
"""

def entance(lst):
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