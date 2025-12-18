"""
QUESTION:
Write a function `find_most_frequent` that takes a list of integers as input and returns a list of the most frequent value(s) in the list. If there are multiple values that occur with the same maximum frequency, return all of them in the list, sorted in descending order. The function should not use any built-in Python functions or libraries, and it should have a time complexity of O(n^2) is not required, however O(n^3) is acceptable where n is the length of the input list.
"""

def find_most_frequent(nums):
    count = {}
    max_count = 0

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] > max_count:
            max_count = count[num]

    most_frequent = []
    for num, freq in count.items():
        if freq == max_count:
            most_frequent.append(num)

    most_frequent.sort(reverse=True)

    return most_frequent