"""
QUESTION:
Given a list of numbers and a target number, write a function `find_three_numbers` that finds all unique combinations of three numbers in the list whose sum is equal to the target number. The function should take the list and target number as parameters, handle duplicate numbers in the list, and return a set of tuples representing the unique combinations.
"""

def find_three_numbers(numbers, target):
    numbers.sort()
    combinations = set()

    for i in range(len(numbers)-2):
        num1 = numbers[i]
        left = i + 1
        right = len(numbers) - 1

        while left < right:
            num2 = numbers[left]
            num3 = numbers[right]

            if num1 + num2 + num3 == target:
                combinations.add((num1, num2, num3))
                left += 1
                right -= 1

            elif num1 + num2 + num3 < target:
                left += 1

            else:
                right -= 1

    return combinations