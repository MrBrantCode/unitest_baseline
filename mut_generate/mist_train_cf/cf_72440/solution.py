"""
QUESTION:
Write a function named `find_uneven` that takes an array of integers as input and returns all integers with uneven frequencies in the order of their first appearance. Uneven frequency means the count of the integer is not divisible by 2. The function should have a time complexity of O(n), where n is the size of the input array.
"""

def find_uneven(arr):
    counter = {}
    result = []

    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for num in arr:
        if counter[num] % 2 != 0 and num not in result:
            result.append(num)

    return result