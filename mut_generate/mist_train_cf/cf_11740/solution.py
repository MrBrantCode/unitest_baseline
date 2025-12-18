"""
QUESTION:
Write a function `most_common_element(lst)` that finds the most frequently occurring element in a given list `lst` with a frequency of at least 2. The function should return the most common element. If there are multiple elements with the same highest frequency, any one of them can be returned. The function should have a time complexity of O(n), where n is the length of the list.
"""

def most_common_element(lst):
    count = {}
    max_count = 0
    most_common = None
    
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        
        if count[num] > max_count and count[num] > 1:
            max_count = count[num]
            most_common = num
    
    return most_common