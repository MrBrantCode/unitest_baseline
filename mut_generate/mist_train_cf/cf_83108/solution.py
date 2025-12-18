"""
QUESTION:
Implement a function called `filter_and_sort` that takes a list of inputs. Ensure the function filters out non-integer values from the list and returns a list of unique integers in ascending order. If non-integer values are found, print a message indicating that the value is not an integer and ignore it. The function should not terminate due to non-integer values.
"""

def filter_and_sort(input_list):
    int_list = []
    for i in input_list:
        if isinstance(i, int):
            int_list.append(i)
        else:
            print("{} is not an integer. Ignoring...".format(i))
    return sorted(set(int_list))