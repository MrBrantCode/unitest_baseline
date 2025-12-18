"""
QUESTION:
Write a function called "find_common_elements" that takes in two sorted arrays as input and returns a new array containing the common elements. The input arrays can have duplicate elements and the output should include all duplicates. The output array should be sorted in ascending order. Do not use any built-in functions or libraries to solve this problem.

Constraints:
- The length of both input arrays will not exceed 10^5.
- The values in the input arrays will be integers between -10^9 and 10^9.
- The output array should have a space complexity of O(n), where n is the number of common elements between the two arrays.
- The time complexity of the solution should be O(n), where n is the maximum length of the two input arrays.
"""

def find_common_elements(arr1, arr2):
    # Initialize two pointers, one for each array
    pointer1 = 0
    pointer2 = 0

    # Initialize an empty list to store the common elements
    common_elements = []

    # Iterate through both arrays until we reach the end of one of the arrays
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        # If the current elements in both arrays are equal, add it to the common_elements list
        if arr1[pointer1] == arr2[pointer2]:
            common_elements.append(arr1[pointer1])
            pointer1 += 1
            pointer2 += 1
        # If the element in arr1 is smaller, move pointer1 to the next element
        elif arr1[pointer1] < arr2[pointer2]:
            pointer1 += 1
        # If the element in arr2 is smaller, move pointer2 to the next element
        else:
            pointer2 += 1

    return common_elements