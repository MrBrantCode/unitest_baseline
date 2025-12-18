"""
QUESTION:
Create a function `mean(input_list)` that calculates the mean of the numbers in the input list, rounded to the nearest integer. The function should handle cases where the input list is empty or contains non-numeric values, and should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def mean(input_list):
    if not input_list:
        return 0
    
    total = 0
    count = 0
    
    for num in input_list:
        if isinstance(num, (int, float)):
            total += num
            count += 1
    
    if count == 0:
        return 0
    
    mean = total / count
    return round(mean)