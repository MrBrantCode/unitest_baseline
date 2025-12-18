"""
QUESTION:
Design a function named `partition_numbers` that takes a list of integers as input, partitions the list into four groups of numbers: those divisible by 3, those divisible by 5, those divisible by 7, and those divisible by both 3 and 5. The function should also calculate the sum and average of each group. The function should return a dictionary containing the numbers in each group, the sum of each group, and the average of each group.
"""

def partition_numbers(numbers):
    # Initialize empty lists for each group
    divisible_by_3 = []
    divisible_by_5 = []
    divisible_by_7 = []
    divisible_by_3_and_5 = []

    # Iterate over the input numbers
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            divisible_by_3_and_5.append(num)
        elif num % 3 == 0:
            divisible_by_3.append(num)
        elif num % 5 == 0:
            divisible_by_5.append(num)
        elif num % 7 == 0:
            divisible_by_7.append(num)

    # Calculate the sum and average of each group
    sum_divisible_by_3 = sum(divisible_by_3)
    avg_divisible_by_3 = sum_divisible_by_3 / len(divisible_by_3) if len(divisible_by_3) > 0 else 0

    sum_divisible_by_5 = sum(divisible_by_5)
    avg_divisible_by_5 = sum_divisible_by_5 / len(divisible_by_5) if len(divisible_by_5) > 0 else 0

    sum_divisible_by_7 = sum(divisible_by_7)
    avg_divisible_by_7 = sum_divisible_by_7 / len(divisible_by_7) if len(divisible_by_7) > 0 else 0

    sum_divisible_by_3_and_5 = sum(divisible_by_3_and_5)
    avg_divisible_by_3_and_5 = sum_divisible_by_3_and_5 / len(divisible_by_3_and_5) if len(divisible_by_3_and_5) > 0 else 0

    # Store the results in a dictionary
    result = {
        "divisible_by_3": divisible_by_3,
        "sum_divisible_by_3": sum_divisible_by_3,
        "avg_divisible_by_3": avg_divisible_by_3,

        "divisible_by_5": divisible_by_5,
        "sum_divisible_by_5": sum_divisible_by_5,
        "avg_divisible_by_5": avg_divisible_by_5,

        "divisible_by_7": divisible_by_7,
        "sum_divisible_by_7": sum_divisible_by_7,
        "avg_divisible_by_7": avg_divisible_by_7,

        "divisible_by_3_and_5": divisible_by_3_and_5,
        "sum_divisible_by_3_and_5": sum_divisible_by_3_and_5,
        "avg_divisible_by_3_and_5": avg_divisible_by_3_and_5
    }

    return result