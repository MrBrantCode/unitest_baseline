"""
QUESTION:
Write a function `reverse_concatenate_max` that takes two lists of integers as input and returns a string. The function should:

* Compare the two lists element by element and create a new list containing the maximum value between the two corresponding elements at each index.
* Reverse the order of both lists and concatenate them along with the new list created in the previous step.
* Convert each element of the concatenated list into a string.
* Join all elements of the new list into one string using a comma as a separator.

Restrictions:
* The input lists must be of equal length.
* The input lists must contain only integers.

In case of any error, the function should return an error message.
"""

def reverse_concatenate_max(list1, list2):
    if len(list1) != len(list2):
        return "Error: Input lists must be of equal length."
    for i in (list1+list2):
        if not isinstance(i, int):
            return "Error: Input lists must contain only integers."

    l_max = [max(a,b) for a, b in zip(list1, list2)]
    list1.reverse()
    list2.reverse()

    combined_list = list1 + list2 + l_max
    str_list = [str(i) for i in combined_list]

    return ','.join(str_list)