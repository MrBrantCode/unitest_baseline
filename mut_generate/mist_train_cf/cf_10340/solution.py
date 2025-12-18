"""
QUESTION:
Write a function named `find_reverse_difference` that takes a positive integer less than 10^9 as input and returns the absolute difference between the number and its reverse as an integer.
"""

def find_reverse_difference(n):
    # Reverse the number by converting it to a string and reversing it
    reversed_num = int(str(n)[::-1])
    
    # Calculate the absolute difference between the number and its reverse
    difference = abs(n - reversed_num)
    
    return difference