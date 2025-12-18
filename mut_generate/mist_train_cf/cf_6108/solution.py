"""
QUESTION:
Create a function called `print_divisible_by_3` that takes a list of integers as input. The function should print the elements in the list that are divisible by 3, sorted in descending order. If the input list is empty or contains non-integer elements, the function should print a corresponding error message.
"""

def print_divisible_by_3(lst):
    if not lst:
        print("The list is empty.")
        return

    numbers = []
    for num in lst:
        if isinstance(num, int):
            if num % 3 == 0:
                numbers.append(num)
        else:
            print(f"{num} is not an integer.")

    if not numbers:
        print("There are no elements divisible by 3.")
        return

    numbers.sort(reverse=True)
    for num in numbers:
        print(num)