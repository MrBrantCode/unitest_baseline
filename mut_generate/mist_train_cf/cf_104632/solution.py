"""
QUESTION:
Write a function `most_frequent_greater_than_10` that takes a list of integers as input and returns the integer greater than 10 that appears most frequently in the list. If there are multiple integers greater than 10 with the same highest frequency, return any of them.
"""

def most_frequent_greater_than_10(lst):
    # filter numbers greater than 10
    greater_than_10 = [num for num in lst if num > 10]
    
    # count frequency of each number
    frequency = {}
    for num in greater_than_10:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # find the number with the highest frequency
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent