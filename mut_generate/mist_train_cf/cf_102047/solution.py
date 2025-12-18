"""
QUESTION:
Write a function `find_second_last_even` that takes a list of integers as input and prints the second last even number in the list. If there are no even numbers or only one even number in the list, print "No even numbers found".
"""

def find_second_last_even(lst):
    even_count = 0
    second_last_even = None
    for num in reversed(lst):
        if num % 2 == 0:
            even_count += 1
            if even_count == 2:
                second_last_even = num
                break
    if even_count >= 2:
        return second_last_even
    else:
        return "No even numbers found"