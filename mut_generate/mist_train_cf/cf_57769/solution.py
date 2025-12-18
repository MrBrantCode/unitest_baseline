"""
QUESTION:
Develop a Python function called `arrange_nums` that takes a list of mixed data types, filters out non-numerical values, separates the remaining numbers into negative and positive lists, and then sorts the negative numbers in ascending order and the positive numbers in descending order. The function should return the two sorted lists.
"""

def arrange_nums(lst):
    try:
        # Filter out non-numerical values
        lst = [i for i in lst if isinstance(i, (int, float))]

        # Separate positive and negative numbers
        neg_nums = [i for i in lst if i < 0]
        pos_nums = [i for i in lst if i >= 0]

        # Sort the negative numbers in increasing order
        neg_nums.sort()

        # Sort the positive numbers in decreasing order
        pos_nums.sort(reverse=True)

        # Return both lists
        return neg_nums, pos_nums
    except Exception as e:
        print("An exception occurred: ", e)