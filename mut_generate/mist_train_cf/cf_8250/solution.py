"""
QUESTION:
Given two sets SetA and SetB, implement a function find_intersection_sum(SetA, SetB) that calculates the intersection of the two sets, removes duplicates, sorts the elements in descending order, and returns the sum of all elements in the intersection set along with the count of elements divisible by 3 and less than 10.
"""

def find_intersection_sum(SetA, SetB):
    intersection_set = SetA.intersection(SetB)
    intersection_set = set(intersection_set)
    sorted_intersection_set = sorted(intersection_set, reverse=True)
    sum_of_intersection = sum(sorted_intersection_set)
    
    count = 0
    for num in intersection_set:
        if num % 3 == 0 and num < 10:
            count += 1
            
    return sum_of_intersection, count