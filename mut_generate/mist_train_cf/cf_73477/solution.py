"""
QUESTION:
Write a function named `bubble_sort` that takes a list of numbers as input and returns the list sorted in ascending order using the Bubble Sort algorithm. The list may contain a mix of positive and negative integers and floating point numbers.
"""

def bubble_sort(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list) - 1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list