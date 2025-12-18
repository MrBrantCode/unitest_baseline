"""
QUESTION:
Create a function `analyze_numbers` that takes a list of integers as input and returns the median of the sorted list, the number of even numbers, and the number of odd numbers. The input list will have at least 3 elements, and the elements will be in the range of -10^3 to 10^3.
"""

def analyze_numbers(lst):
    # Sort the array.
    lst.sort()
    # Calculate the median.
    n = len(lst)
    median = (lst[(n-1)//2] + lst[n//2]) / 2
    # Calculate the number of even and odd numbers.
    num_even = sum(1 for x in lst if x % 2 == 0)
    num_odd = n - num_even
    # Return the results.
    return median, num_even, num_odd