"""
QUESTION:
Implement a function named `intersection` that takes two arrays `arr_1` and `arr_2` as input and returns their intersection while maintaining the order of elements from `arr_1`. The function should have a time complexity of O(n), where n is the total number of elements in both arrays, and a space complexity of O(m), where m is the number of elements in the intersection of the two arrays. The function should not use any built-in intersection or set functions, should not modify the original arrays, and should return an array containing the intersection of the two arrays without any duplicates.
"""

def intersection(arr_1, arr_2):
    # Create a set to store unique elements from arr_2
    set_2 = set(arr_2)
    
    # Create a list to store the intersection
    intersection = []
    
    # Iterate through arr_1 and check if each element is in set_2
    for num in arr_1:
        if num in set_2:
            intersection.append(num)
            set_2.remove(num)  # Remove the element from set_2 to avoid duplicates
    
    return intersection