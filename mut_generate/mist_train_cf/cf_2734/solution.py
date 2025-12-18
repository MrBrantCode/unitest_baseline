"""
QUESTION:
Create a function called `get_sublist` that takes a list of numbers and two integers, `certain_value` and `divisible_value`, as inputs. This function should return a sublist of numbers from the input list that are greater than `certain_value`, divisible by `divisible_value`, and sorted in descending order. The sublist should not contain any duplicate elements and should have a length between 5 and 15. The solution should have a time complexity of O(n) or less and should not use built-in Python functions such as `filter()`, `sorted()`, list comprehensions, or `set()`.
"""

def get_sublist(lst, certain_value, divisible_value):
    sublist = []
    for num in lst:
        if num > certain_value and num % divisible_value == 0 and num not in sublist:
            sublist.append(num)
            if len(sublist) == 15:
                break

    # Bubble sort the sublist in descending order
    for i in range(len(sublist) - 1):
        for j in range(len(sublist) - 1 - i):
            if sublist[j] < sublist[j+1]:
                sublist[j], sublist[j+1] = sublist[j+1], sublist[j]

    # Remove extra elements if length > 15
    sublist = sublist[:15]

    return sublist