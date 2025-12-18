"""
QUESTION:
Write a function named `swap_for_odds` that takes two non-empty lists of integers `lst1` and `lst2` as input, and returns "YES" if it's possible to swap elements between them to make `lst1` a list of only odd numbers without changing the total sum of elements in both lists, and "NO" otherwise.
"""

def swap_for_odds(lst1, lst2):
    # Calculate the total sum of each list
    total1 = sum(lst1)
    total2 = sum(lst2)
    # Use list comprehension to find the sum of all odd numbers in both lists
    odd_sum1 = sum([i for i in lst1 if i % 2 == 1])
    odd_sum2 = sum([i for i in lst2 if i % 2 == 1])
    # Check if the sum of odd numbers in both lists, plus the even numbers left in
    # the second list (total2 - odd_sum2), equals to the total sum of the first list
    return "YES" if odd_sum1 + (total2 - odd_sum2) * 2 == total1 else "NO"