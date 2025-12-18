"""
QUESTION:
Compute the average of the positive integers greater than 5 in a given list, rounded to the nearest whole number. The output should be a tuple containing the average, the number of positive integers greater than 5, and their sum. If the list is empty or there are no positive integers greater than 5, return (0, 0, 0).

Implement a function named `average_positive_greater_than_five` that takes a list of numbers as input and returns the described tuple.
"""

def average_positive_greater_than_five(numbers):
    # Initialize variables
    sum_positive = 0
    count_positive = 0
    
    # Iterate through the list
    for num in numbers:
        if num > 5:
            sum_positive += num
            count_positive += 1
    
    # Calculate the average
    if count_positive == 0:
        average = 0
    else:
        average = round(sum_positive / count_positive)
    
    return (average, count_positive, sum_positive)