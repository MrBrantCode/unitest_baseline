"""
QUESTION:
Implement a function named `intersection` that takes two arrays `arr_1` and `arr_2` as input and returns their intersection while maintaining the order of elements from `arr_1`. The function should have a time complexity of O(n) and a space complexity of O(m), where n is the total number of elements in both arrays and m is the number of elements in the intersection. The function should handle arrays of any size, including empty arrays, and should not use any built-in intersection or set functions. The function should not modify the original arrays, should return an array containing the intersection of the two arrays without any duplicates, and should maintain the order of elements from the first array in the resulting intersection array.
"""

def intersection(arr_1, arr_2):
    set_2 = set(arr_2)
    intersection = []
    
    for num in arr_1:
        if num in set_2:
            intersection.append(num)
            set_2.remove(num)
    
    return intersection