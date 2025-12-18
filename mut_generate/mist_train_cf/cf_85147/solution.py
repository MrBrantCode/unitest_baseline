"""
QUESTION:
Write a function `subset_sum(lst, target, length)` that uses recursion to find all possible subsets of a given size in the list `lst` that add up to the target sum `target`. The function should print all such subsets if they exist. The list `lst` contains only positive numbers.
"""

def subset_sum(lst, target, length, partial=[]):
    s = sum(partial)

    # Check if the partial sum is equals to target
    if s == target and len(partial)==length:
        print("Subset found: ", partial)
    if s >= target:
        return  # If we reach the target sum, we return

    for i in range(len(lst)):
        n = lst[i]
        remaining = lst[i+1:]
        subset_sum(remaining, target, length, partial + [n])