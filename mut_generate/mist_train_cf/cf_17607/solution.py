"""
QUESTION:
Create a function named `get_sublist` that takes a list of integers `lst`, an integer `threshold`, and an integer `divisor` as parameters. The function should return a sublist containing elements from `lst` that are greater than `threshold` and divisible by `divisor`, sorted in descending order. The solution must not use built-in Python functions such as `filter()`, `sorted()`, or list comprehensions.
"""

def get_sublist(lst, threshold, divisor):
    # Create an empty sublist to store the filtered elements
    sublist = []

    # Iterate over the original list
    for element in lst:
        # Check if the element is greater than the threshold and divisible by the divisor
        if element > threshold and element % divisor == 0:
            # Append the element to the sublist
            sublist.append(element)

    # Sort the sublist in descending order
    for i in range(len(sublist)):
        for j in range(i + 1, len(sublist)):
            if sublist[i] < sublist[j]:
                sublist[i], sublist[j] = sublist[j], sublist[i]

    # Return the sorted sublist
    return sublist