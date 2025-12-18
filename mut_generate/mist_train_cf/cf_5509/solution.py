"""
QUESTION:
Write a function called `calculate_average` that takes an array of numbers as input and returns the average of only the positive integers in the array, rounded to the nearest whole number. The function should have a time complexity of O(n) and a space complexity of O(1). If the array does not contain any positive integers, the function should return 0.
"""

def entrance(arr):
    count = 0
    total = 0

    for num in arr:
        if num > 0:
            count += 1
            total += num

    if count == 0:
        return 0
    
    average = total / count
    rounded_average = round(average)

    return rounded_average