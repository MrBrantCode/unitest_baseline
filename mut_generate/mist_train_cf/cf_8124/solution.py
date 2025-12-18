"""
QUESTION:
Create a recursive function `count_divisible(numbers, divisible_number, index=0, count=0)` that takes a list of numbers and a divisible number as input, and returns the count of numbers in the list that are divisible by the given number. The function must start checking the numbers from the beginning of the list and use an index parameter to keep track of the current number being checked.
"""

def count_divisible(numbers, divisible_number, index=0, count=0):
    if index == len(numbers):
        return count
    if numbers[index] % divisible_number == 0:
        count += 1
    return count_divisible(numbers, divisible_number, index + 1, count)