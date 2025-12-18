"""
QUESTION:
Write a function `third_smallest` that finds the third smallest unique number in an unsorted list of integers. The list may contain duplicate values, negative integers, and may have less than three unique elements. If the list has less than three unique elements, return a message indicating this.
"""

def third_smallest(numbers):
    numbers = list(set(numbers)) 
    numbers.sort() 
    if len(numbers) < 3:
        return "Too few unique numbers in the list."
    else:
        return numbers[2]