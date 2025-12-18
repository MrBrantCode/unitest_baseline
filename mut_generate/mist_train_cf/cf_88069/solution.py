"""
QUESTION:
Create a function named `find_duplicate_elements` that takes a list of integers `lst` as input and returns a list of all duplicate elements found in the list. The input list can contain negative numbers and zero, in addition to positive numbers. The function should have a time complexity of O(n), where n is the number of elements in the input list.
"""

def find_duplicate_elements(lst):
    duplicates = []
    count = {}
    
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)
    
    return duplicates