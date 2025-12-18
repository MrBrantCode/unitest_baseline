"""
QUESTION:
Create a function called find_unique_elements that takes in a list of integers and returns a list of elements that appear exactly once in the list, excluding any duplicates. The function should handle positive and negative numbers, zero, and empty input lists, and it should return the elements in the order of their first occurrence in the input list. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.
"""

def find_unique_elements(arr):
    if not arr:  # handle case of empty input array
        return []
    
    frequency = {}  # dictionary to store the frequency of elements
    
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1  # update the frequency of each element
    
    result = []  # list to store the unique elements
    
    for num in arr:
        if frequency[num] == 1:
            result.append(num)  # add the element to the result list if its frequency is 1
    
    return result