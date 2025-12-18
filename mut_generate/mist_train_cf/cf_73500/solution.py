"""
QUESTION:
Design a function named `get_median` that takes ten integer parameters and returns their median without using any sort, comparison, or conditional operators, and without any library functions. The function should handle any combination of integers, including duplicates and unsorted numbers.
"""

def get_median(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10):
    integers = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
    integer_map = {}
    
    for integer in integers:
        if integer in integer_map:
            integer_map[integer] += 1
        else:
            integer_map[integer] = 1

    count = 0

    for key in integer_map:
        count += integer_map[key]
        if count >= 5:
            return key