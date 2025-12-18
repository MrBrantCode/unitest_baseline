"""
QUESTION:
Create a Python function `find_bottleneck(lst)` that finds the smallest "bottleneck" element in a list of integers. A bottleneck element is defined as an element where the sum of all elements to the left is equal to the product of the non-zero elements to the right. If no bottleneck is found, return -1.
"""

def find_bottleneck(lst):
    bottlenecks = []  # List to hold all bottleneck elements
    for i in range(len(lst) - 1):
        sum_left = sum(lst[:i])  # Sum of elements on the left
        prod_right = 1  # Product of non-zero elements on the right
        # Calculate product of non-zero elements on the right
        for j in range(i + 1, len(lst)):
            if lst[j] != 0:
                prod_right *= lst[j]
        # Check if current element is a bottleneck
        if sum_left == prod_right:
            bottlenecks.append(lst[i])
    # Return the minimum bottleneck if any, otherwise return -1
    if not bottlenecks:
        return -1
    else:
        return min(bottlenecks)