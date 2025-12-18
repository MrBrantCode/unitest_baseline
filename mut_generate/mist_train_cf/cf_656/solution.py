"""
QUESTION:
Write a function named `find_max_min_avg` to find the maximum, minimum, and average values in an array of numbers. The function should not use any built-in functions or methods to sort or find the maximum, minimum, or average values. The solution should have a time complexity of O(n), where n is the length of the input array, and use constant space. Additionally, the solution should not use any loops or higher-order functions, and instead, use recursion and basic operations like arithmetic and conditional statements.
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

            # Update max value if necessary
            if numbers[index] > max_value:
                max_value = numbers[index]

            # Update min value if necessary
            if numbers[index] < min_value:
                min_value = numbers[index]

            # Update sum value
            sum_value += numbers[index]

            # Recursive call with next index
            helper(numbers, index + 1)

        helper(numbers, 1)
        avg_value = sum_value / len(numbers)
        return max_value, min_value, avg_value