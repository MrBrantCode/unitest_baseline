"""
QUESTION:
Write a function `count_and_print_even_elements(arr)` that takes an array of integers as input, prints all the even elements in the array, and returns the count of even elements encountered. The function should have a time complexity of O(n), where n is the size of the array, and it should not use any built-in functions or libraries that directly check the divisibility of a number by 2, the modulus operator (%), or bitwise operations. The function should handle both positive and negative integers and floating-point numbers in the array.
"""

def entrance(arr):
    count = 0
    index = 0
    while index < len(arr):
        element = arr[index]
        if int(element) == element and int(element / 2) * 2 == element:
            print(element)
            count += 1
        index += 1
    return count