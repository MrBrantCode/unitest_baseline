"""
QUESTION:
Write a function `count_and_print_even_elements(arr)` that takes an array of integers as input and prints only the even elements while keeping track of the number of even elements encountered. The function must have a time complexity of O(n), where n is the size of the array, and cannot use any built-in functions or libraries that directly check the divisibility of a number by 2, or any additional data structures or arrays to store the even elements. The function should be able to handle both positive and negative integers in the array and return the total count of even elements encountered.
"""

def count_and_print_even_elements(arr):
    count = 0
    index = 0
    
    while index < len(arr):
        if arr[index] % 2 == 0:
            print(arr[index])
            count += 1
        index += 1
    
    return count