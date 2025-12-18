"""
QUESTION:
Find the top 3 highest numbers in an array of up to 1000 elements without using any sorting algorithm. The function should return the three highest numbers in descending order. The function name is `find_top_3_highest_numbers` and it takes an array as input.
"""

def find_top_3_highest_numbers(arr):
    highest_numbers = [float('-inf')] * 3

    for num in arr:
        if num > highest_numbers[0]:
            highest_numbers[2] = highest_numbers[1]
            highest_numbers[1] = highest_numbers[0]
            highest_numbers[0] = num
        elif num > highest_numbers[1]:
            highest_numbers[2] = highest_numbers[1]
            highest_numbers[1] = num
        elif num > highest_numbers[2]:
            highest_numbers[2] = num

    return highest_numbers