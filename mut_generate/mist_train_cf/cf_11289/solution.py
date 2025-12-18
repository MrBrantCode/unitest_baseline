"""
QUESTION:
Design a function `calculate_intersection` that takes two lists, List1 and List2, as input and returns their intersection, including duplicates, in a list. The function should have a time complexity of O(n+m), where n and m are the lengths of List1 and List2, respectively.
"""

def calculate_intersection(List1, List2):
    intersection_dict = {}
    intersection_list = []

    for num in List1:
        if num not in intersection_dict:
            intersection_dict[num] = 1
        else:
            intersection_dict[num] += 1

    for num in List2:
        if num in intersection_dict and intersection_dict[num] > 0:
            intersection_list.append(num)
            intersection_dict[num] -= 1

    return intersection_list