"""
QUESTION:
Write a function `intersect(lst1, lst2)` that takes two sorted lists of integers as input and returns their intersection without using built-in set operations or looping constructs. The function should handle duplicates and negative integers, and it should not remove duplicates from the lists.
"""

def intersect(lst1, lst2):
    if lst1 and lst2:  
        head1, *tail1 = lst1
        head2, *tail2 = lst2
        if head1 == head2:
            return [head1] + intersect(tail1, tail2)
        elif head1 < head2:
            return intersect(tail1, lst2)
        else:
            return intersect(lst1, tail2)
    else:
        return []