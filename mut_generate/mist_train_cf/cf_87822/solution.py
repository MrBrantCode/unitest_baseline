"""
QUESTION:
Calculate the average of non-negative numbers in an array and round to the nearest whole number. 

Function name: calculate_average

Input: An array of integers
Output: The average of the non-negative numbers in the array, rounded to the nearest whole number, or 0 if all numbers in the array are negative.

Restrictions: Exclude negative numbers from the calculation.
"""

def calculate_average(arr):
    total_sum = 0
    count = 0

    for num in arr:
        if num >= 0:
            total_sum += num
            count += 1

    if count > 0:
        average = round(total_sum / count)
        return average
    else:
        return 0