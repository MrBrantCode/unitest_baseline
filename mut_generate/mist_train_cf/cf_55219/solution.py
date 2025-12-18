"""
QUESTION:
Write a function `exchange(lst1, lst2)` that takes two lists of integers as input and returns a string 'YES' if it's possible to swap elements between the two lists to make the first list contain only even numbers, and 'NO' otherwise. The function should return 'NO' if the number of odd numbers in the first list is greater than the number of even numbers in the second list, or if the sum of the odd numbers in the first list and the even numbers in the second list is less than the sum of the even numbers in the first list and the odd numbers in the second list.
"""

def exchange(lst1, lst2):
    lst1_even = [num for num in lst1 if num % 2 == 0]
    lst1_odd = [num for num in lst1 if num % 2 != 0]
    lst2_even = [num for num in lst2 if num % 2 == 0]
    lst2_odd = [num for num in lst2 if num % 2 != 0]

    sum_lst1_odd = sum(lst1_odd)
    sum_lst1_even = sum(lst1_even)
    sum_lst2_odd = sum(lst2_odd)
    sum_lst2_even = sum(lst2_even)

    if len(lst1_odd) > len(lst2_even) or sum_lst1_odd + sum_lst2_even < sum_lst1_even + sum_lst2_odd:
        return "NO"

    return "YES"