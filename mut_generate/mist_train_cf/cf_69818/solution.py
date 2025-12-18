"""
QUESTION:
Write a function `calculate_values(numbers)` that takes a list of integers as input and returns the highest, lowest, and median values. The function should be efficient enough to handle large inputs. Assume the input list contains at least one element.
"""

def calculate_values(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[int(len(numbers)/2)-1] + numbers[int(len(numbers)/2)]) / 2
    else:
        median = numbers[int(len(numbers)/2)]
    return highest, lowest, median