"""
QUESTION:
Calculate the sum of the first 3 unique numbers in a given list of integers. If there are less than 3 unique numbers, calculate the sum of all unique numbers. Implement this functionality in a function named `calculate_sum_unique_numbers` that takes a list of integers as input and returns the calculated sum. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def calculate_sum_unique_numbers(lst):
    unique_numbers = set()
    counts = {}

    for num in lst:
        if num not in unique_numbers:
            unique_numbers.add(num)
            counts[num] = 1
        else:
            counts[num] += 1

    total_sum = 0
    count = 0
    for num in lst:
        if num in unique_numbers and counts[num] > 0:
            total_sum += num
            counts[num] -= 1
            count += 1
            if count == 3:
                break

    return total_sum