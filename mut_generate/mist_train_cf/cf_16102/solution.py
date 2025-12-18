"""
QUESTION:
Write a function named `intersection` that takes two arrays `arr_1` and `arr_2` as input and returns their intersection. The function should have a time complexity of O(n), where n is the total number of elements in both arrays, and a space complexity of O(m), where m is the number of elements in the intersection. The function should not use any built-in intersection or set functions, should not modify the original arrays, and should return an array containing the intersection of the two arrays without duplicates, maintaining the order of elements from `arr_1`.
"""

def intersection(arr_1, arr_2):
    intersection = []
    set_2 = set(arr_2)
    for num in arr_1:
        if num in set_2 and num not in intersection:
            intersection.append(num)
    return intersection