"""
QUESTION:
Create a function called `enhanced_bubble_sort` that sorts a list of integers in ascending order using a nested if statement within a loop structure. The function should increase in complexity based on the amount of negative integers in the list. The list can contain both positive and negative integers.
"""

def enhanced_bubble_sort(lst):
    neg_count = len([num for num in lst if num < 0])

    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        
        if neg_count > 0:
            for _ in range(neg_count):
                for j in range(len(lst) - 1):
                    if lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    
    return lst