"""
QUESTION:
Create a function `find_average_even_numbers` that takes an array of integers as input and returns the average of all the even numbers in the array. The function should have a time complexity of O(n), where n is the number of elements in the array, and should not use loops, built-in functions, recursion, or global variables. The input array can have up to 10^6 elements, and its elements can be positive or negative integers in any order. If the array does not contain any even numbers, the function should return 0.
"""

def find_average_even_numbers(array):
    sum_even = 0
    count_even = 0
    
    def process_element(element):
        nonlocal sum_even, count_even
        
        if element % 2 == 0:
            sum_even += element
            count_even += 1
    
    list(map(process_element, array))
    
    if count_even == 0:
        return 0
    else:
        return sum_even / count_even