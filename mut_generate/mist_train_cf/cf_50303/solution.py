"""
QUESTION:
Create a function named `sort_positives_and_calculate_averages` that takes a list of numbers as input, returns a tuple containing the sorted list of positive numbers, the average of these positive numbers rounded to two decimal places, and the average of the remaining numbers rounded to two decimal places.
"""

def sort_positives_and_calculate_averages(l: list):
    """
    Return the positive numbers from the input list, sorted in ascending order.
    Also, separately calculate the average of these positive numbers, and the average of the remaining numbers.
    """

    # Separate positive and non-positive numbers to different lists
    positive_nums = [num for num in l if num > 0]
    non_positive_nums = [num for num in l if num <= 0]

    # If there are positive numbers, sort them and calculate their average
    if positive_nums:
        positive_nums.sort()
        positive_avg = sum(positive_nums) / len(positive_nums)
    else:
        positive_avg = 0

    # If there are non-positive numbers, calculate their average
    if non_positive_nums:
        non_positive_avg = sum(non_positive_nums) / len(non_positive_nums)
    else:
        non_positive_avg = 0

    return positive_nums, round(positive_avg, 2), round(non_positive_avg, 2)