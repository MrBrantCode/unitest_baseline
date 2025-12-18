"""
QUESTION:
Implement a function named `find_intersection` that takes two arrays `arr_1` and `arr_2` as input and returns their intersection. The function should have a time complexity of O(n), where n is the total number of elements in both arrays, and a space complexity of O(m), where m is the number of elements in the intersection of the two arrays. The function should be able to handle arrays of any size, including empty arrays.
"""

def find_intersection(arr_1, arr_2):
    # Create a hash set to store the elements of arr_1
    set_1 = set(arr_1)
    
    # Create a list to store the intersection of the two arrays
    intersection = []
    
    # Iterate over arr_2 and check if each element is in set_1
    for num in arr_2:
        if num in set_1:
            intersection.append(num)
    
    return intersection