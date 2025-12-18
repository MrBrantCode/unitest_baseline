"""
QUESTION:
Write a function `find_highest_number` that takes a list of numbers as input and returns the highest number in the list. If the list is empty, the function should print "Error: The list is empty" instead of returning a value.
"""

def find_highest_number(numbers):
    if not numbers:
        print("Error: The list is empty.")
        return

    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num

    return highest