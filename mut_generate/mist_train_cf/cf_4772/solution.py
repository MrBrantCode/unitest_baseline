"""
QUESTION:
Write a function `find_average_even_numbers` that calculates the average of all the even numbers in a given array. The function should have a time complexity of O(n), where n is the number of elements in the array, and should not use recursion, global variables, built-in functions, or loops. The array can contain up to 10^6 positive or negative integers in any order. If there are no even numbers in the array, the function should return 0.
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