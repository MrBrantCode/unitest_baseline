"""
QUESTION:
Write a function named `find_max_min_avg` that takes an array of numbers as input and returns the maximum, minimum, and average values. The function must have a time complexity of O(n), where n is the length of the input array, and use constant space. Do not use any built-in functions or methods to sort or find the maximum, minimum, or average values.
"""

def find_max_min_avg(numbers):
    if len(numbers) == 0:
        return None, None, None
    else:
        max_value = numbers[0]
        min_value = numbers[0]
        sum_value = numbers[0]

        def helper(numbers, index):
            nonlocal max_value, min_value, sum_value

            if index == len(numbers):
                return

            if numbers[index] > max_value:
                max_value = numbers[index]

            if numbers[index] < min_value:
                min_value = numbers[index]

            sum_value += numbers[index]
            helper(numbers, index + 1)

        helper(numbers, 1)
        avg_value = sum_value / len(numbers)
        return max_value, min_value, avg_value