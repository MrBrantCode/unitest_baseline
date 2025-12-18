"""
QUESTION:
Write a function named `count_elements` that takes a list as input and returns a list of tuples, where each tuple contains an element from the input list and its count in descending order of count. 

The function should handle empty lists, lists with duplicate elements, and lists with mixed data types, and it should not use any built-in functions or methods to count the occurrences of elements. The time complexity of the function should be O(n^2) or better.
"""

def count_elements(my_list):
    if len(my_list) == 0:
        return []
    
    counts = []
    for element in my_list:
        found = False
        for i in range(len(counts)):
            if counts[i][0] == element:
                counts[i] = (element, counts[i][1] + 1)
                found = True
                break
        if not found:
            counts.append((element, 1))
    
    counts.sort(key=lambda x: x[1], reverse=True)
    
    return counts