"""
QUESTION:
Write a function named `count_unique_elements` that takes a list of numbers as input and returns a list of unique elements in the order of their first occurrence and a dictionary with the frequency of each unique element. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the input list. Do not use any built-in functions or libraries that directly solve the problem.
"""

def count_unique_elements(list_of_nums):
    unique_elements = []
    element_frequency = {}
    
    for num in list_of_nums:
        if num not in unique_elements:
            unique_elements.append(num)
            element_frequency[num] = 1
        else:
            element_frequency[num] += 1
    
    return unique_elements, element_frequency