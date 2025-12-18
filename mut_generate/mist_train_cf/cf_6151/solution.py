"""
QUESTION:
Create a function named `count_elements` that takes a list containing integers, floats, or strings as input and returns a list of tuples. Each tuple should contain an element from the input list and its count, sorted in descending order of count. The function should not use any built-in functions or methods to count the occurrences of elements and should have a time complexity of O(n^2) or better. It should handle empty lists, lists with a large number of elements, duplicate elements, and mixed data types.
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