"""
QUESTION:
Create a function named `find_second_most_frequent` that takes a list of integers as input. The list contains integers ranging from 0 to 1000 and has a length of at least 100. The function should return the second most frequent element in the list with a time complexity of O(n), where n is the length of the list.
"""

def find_second_most_frequent(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    most_frequent = None
    second_most_frequent = None

    for num, count in counts.items():
        if most_frequent is None or count > counts[most_frequent]:
            second_most_frequent = most_frequent
            most_frequent = num
        elif second_most_frequent is None or count > counts[second_most_frequent]:
            second_most_frequent = num

    return second_most_frequent