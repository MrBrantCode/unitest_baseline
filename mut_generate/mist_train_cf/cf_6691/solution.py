"""
QUESTION:
Write a function `count_and_print_even_elements(arr)` that takes an array of numbers as input and prints all the even integers in the array while keeping track of the number of even elements encountered. The function should return the count of even elements. The solution should have a time complexity of O(n), where n is the size of the array, and should not use any built-in functions, libraries, modulus operator (%), or bitwise operations to check divisibility by 2. It should also handle both positive and negative integers, as well as floating-point numbers.
"""

def count_and_print_even_elements(arr):
    count = 0
    index = 0
    while index < len(arr):
        element = arr[index]
        if int(element) == element and int(element / 2) * 2 == element:
            print(element)
            count += 1
        index += 1
    return count