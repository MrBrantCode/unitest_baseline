"""
QUESTION:
Write a function `find_even_numbers` that takes a list of integers as input, finds all even numbers in the list, sorts them in ascending order without using any built-in sorting functions or methods, and returns the sorted even numbers.
"""

def find_even_numbers(list_of_ints):
    even_numbers = []
    for num in list_of_ints:
        if num % 2 == 0:
            even_numbers.append(num)

    # Sorting the even_numbers list in ascending order using bubble sort
    n = len(even_numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if even_numbers[j] > even_numbers[j + 1]:
                even_numbers[j], even_numbers[j + 1] = even_numbers[j + 1], even_numbers[j]

    return even_numbers