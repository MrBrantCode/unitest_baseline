"""
QUESTION:
Write a function called "find_common_prime_elements" that takes in two sorted arrays as input and returns a new array containing the common prime elements. The input arrays may have duplicate elements and the output should include all duplicates. The output array should be sorted in ascending order. Assume the input arrays are sorted in ascending order and the prime numbers in the input arrays are less than or equal to 100. The solution should have a time complexity of O(n), where n is the maximum length of the two input arrays, and a space complexity of O(n), where n is the number of common prime elements between the two arrays. Do not use any built-in functions or libraries to solve this problem.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_common_prime_elements(arr1, arr2):
    result = []
    pointer1 = 0
    pointer2 = 0
    
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] == arr2[pointer2] and is_prime(arr1[pointer1]):
            result.append(arr1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif arr1[pointer1] < arr2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
            
    return result