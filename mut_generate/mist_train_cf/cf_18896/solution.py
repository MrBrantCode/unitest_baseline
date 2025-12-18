"""
QUESTION:
Create a function `cumulative_sum_reverse` that calculates the cumulative sum of a list of positive integers greater than 1, excluding any negative numbers and non-integer elements. The function should remove duplicate elements from the list, sort the remaining elements in descending order, and return the cumulative sum in reverse order. If the input list contains any invalid elements, the function should return an error message.
"""

def cumulative_sum_reverse(lst):
    # Check for negative numbers and non-integer elements
    for num in lst:
        if num < 0 or type(num) != int or num <= 1:
            return "Error: Input list should only contain positive integers greater than 1."

    # Remove duplicate elements
    lst = list(set(lst))

    # Sort the list in descending order
    lst.sort(reverse=True)

    # Calculate the cumulative sum in reverse order
    cumulative_sum = []
    current_sum = 0
    for num in reversed(lst):
        current_sum += num
        cumulative_sum.append(current_sum)

    return cumulative_sum