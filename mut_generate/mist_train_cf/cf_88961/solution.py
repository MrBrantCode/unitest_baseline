"""
QUESTION:
Implement a function `print_list` that takes a list of integers as input, where the list is sorted in non-decreasing order and its length is between 1 and 10^6. The function should check if the list is sorted in non-decreasing order. If the list is sorted, it should print the even numbers in the list in reverse order, followed by the total number of even numbers found. If the list is not sorted, it should print an error message and return without printing the even numbers. The function should have a time complexity of O(n), where n is the length of the input list, and use only O(1) additional space.
"""

from typing import List

def print_list(list: List[int]) -> None:
    # Check if the list is sorted in non-decreasing order
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            print("List is not sorted in non-decreasing order.")
            return
    
    # Print the even numbers in reverse order
    even_count = 0
    for num in reversed(list):
        if num % 2 == 0:
            print(num)
            even_count += 1
    
    # Print the total number of even numbers found
    print("Total number of even numbers found:", even_count)