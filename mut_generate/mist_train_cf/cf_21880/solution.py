"""
QUESTION:
Write a function `find_divisible_numbers(numbers)` that takes a list of integers as input and returns the average, minimum, and maximum of the numbers that are divisible by both 3 and 7, as well as the number of occurrences of each unique number divisible by both 3 and 7 in the list. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def find_divisible_numbers(numbers):
    count = {}
    divisible_nums = []

    for num in numbers:
        if num % 3 == 0 and num % 7 == 0:
            divisible_nums.append(num)
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

    divisible_nums = sorted(divisible_nums)
    average = sum(divisible_nums) / len(divisible_nums)
    minimum = min(divisible_nums)
    maximum = max(divisible_nums)

    return average, minimum, maximum, count