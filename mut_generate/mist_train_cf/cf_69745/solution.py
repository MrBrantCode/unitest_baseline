"""
QUESTION:
Create a function named `my_sorting_algorithm` that takes a list of integers as input. Sort the list in ascending order, but with the restriction that all even numbers must come before all odd numbers.
"""

def my_sorting_algorithm(my_list):
    # Separate numbers into odd and even numbers
    odd_numbers = [num for num in my_list if num % 2 != 0]
    even_numbers = [num for num in my_list if num % 2 == 0]

    # Implement bubble sort for both lists
    for i in range(len(odd_numbers) - 1):
        for j in range(len(odd_numbers) - 1):
            if odd_numbers[j] > odd_numbers[j + 1]:
                odd_numbers[j], odd_numbers[j + 1] = odd_numbers[j + 1], odd_numbers[j]

    for i in range(len(even_numbers) - 1):
        for j in range(len(even_numbers) - 1):
            if even_numbers[j] > even_numbers[j + 1]:
                even_numbers[j], even_numbers[j + 1] = even_numbers[j + 1], even_numbers[j]

    # Return the combined list of sorted even and odd numbers
    return even_numbers + odd_numbers