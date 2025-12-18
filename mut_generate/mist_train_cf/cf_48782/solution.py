"""
QUESTION:
Design a function named `exchange` that takes two lists of integers, `lst1` and `lst2`, as input parameters. The function should determine if it is possible to swap elements between `lst1` and `lst2` to make `lst1` contain only even numbers while keeping the total sum of both lists unchanged. The function should return "YES" if the transformation is feasible and "NO" otherwise. There are no constraints on the number of swaps, and the input lists will always have at least one element.
"""

def exchange(lst1, lst2):
    """Swaps elements between two lists to make first list contain only even numbers."""
    
    #create even and odd lists
    lst1_even = [i for i in lst1 if i % 2 == 0]
    lst1_odd = [i for i in lst1 if i % 2 != 0]
    lst2_even = [i for i in lst2 if i % 2 == 0]
    lst2_odd = [i for i in lst2 if i % 2 != 0]

    #if there are more odd numbers in the first list than even numbers in the second,
    # or the sum of the odd numbers in the first list and the even numbers in the second
    # is less than the sum of the even numbers in the first list and odd numbers in the second,
    # then it is impossible to make the first list contain only even numbers
    if len(lst1_odd) > len(lst2_even) or sum(lst1_odd) + sum(lst2_even) < sum(lst1_even) + sum(lst2_odd):
        return 'NO'

    #else, return 'YES'
    return 'YES'