"""
QUESTION:
Create a function named `find_even_numbers` that takes a list of integers and/or non-integer values as input. The function should return a tuple where the first element is a list of even integers from the input list, sorted in descending order, and the second element is the sum of all even integers. The function must handle non-numeric inputs without throwing exceptions.
"""

def find_even_numbers(input_list):
    even_numbers = []
    even_sum = 0
    for i in input_list:
        if isinstance(i, int):
            if i % 2 == 0:
                even_numbers.append(i)
                even_sum += i
    even_numbers.sort(reverse=True)
    return (even_numbers, even_sum)