"""
QUESTION:
Write a function named `exchange` that takes two integer lists `lst1` and `lst2` as inputs and returns "YES" if it's possible to make all elements in `lst1` even by swapping elements between the lists while preserving the same overall sum, and "NO" otherwise. The function should consider all possible swaps between the lists, without any restriction on the number of swaps.
"""

def exchange(lst1, lst2):
    # First, calculate the sum of both lists
    sum_lst1 = sum(lst1)
    sum_lst2 = sum(lst2)

    # If lists' sums are not the same, it's no possible to make lst1 all even keeping the same overall sum
    if sum_lst1 != sum_lst2: return "NO"

    # Now check if it's possible to make lst1 all even by swapping elements between the lists
    # We just need to check if at least one odd number on lst1 has a corresponding even number on lst2
    # What this means: for every odd number on lst1, there must be even a number on lst2 that subtracted by it results an odd number
    for num1 in lst1:
        if num1 % 2:
            for num2 in lst2:
              if num2 % 2 == 0: # Is num2 even?
                if (num2 - num1) % 2: # Is the difference between num2 and num1 odd?
                    return "YES"
    return "NO"