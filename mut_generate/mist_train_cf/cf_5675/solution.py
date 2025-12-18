"""
QUESTION:
Create a function `sort_even_numbers(numbers)` that takes a list of numbers as input and returns a new list containing only the even numbers (excluding negative numbers) in descending order. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions or data structures.
"""

def sort_even_numbers(numbers):
    # Create a new list to store the even numbers
    even_numbers = []

    # Iterate through each number in the input list
    for number in numbers:
        # Check if the number is even and positive
        if number % 2 == 0 and number >= 0:
            # Add the number to the even_numbers list
            even_numbers.append(number)

    # Sort the even_numbers list in descending order using bubble sort
    for i in range(len(even_numbers) - 1):
        for j in range(len(even_numbers) - 1 - i):
            if even_numbers[j] < even_numbers[j + 1]:
                even_numbers[j], even_numbers[j + 1] = even_numbers[j + 1], even_numbers[j]

    return even_numbers