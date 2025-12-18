"""
QUESTION:
Write a function `count_and_print_even_elements(arr)` that traverses through an array `arr`, prints only the even elements, and returns the count of even elements encountered. The function must have a time complexity of O(n), where n is the size of the array, and cannot use built-in functions or libraries to check divisibility by 2, or additional data structures or arrays. The function should handle both positive and negative integers in the array.
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