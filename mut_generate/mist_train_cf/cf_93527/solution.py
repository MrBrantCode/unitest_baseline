"""
QUESTION:
Write a function called `find_most_frequent_number` that takes a list of integers as input and returns the most frequent number greater than 100. The list can contain up to 10^6 numbers, and the numbers are guaranteed to be integers between 1 and 10^6. The function should have a time complexity of O(n) and a space complexity of O(m), where n is the number of elements in the list and m is the number of unique numbers greater than 100 in the list.
"""

def find_most_frequent_number(numbers):
    frequency = {}
    max_frequency = 0
    most_frequent_number = None

    for number in numbers:
        if number > 100:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1

            if frequency[number] > max_frequency:
                max_frequency = frequency[number]
                most_frequent_number = number

    return most_frequent_number