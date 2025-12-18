"""
QUESTION:
Create a function named "get_sublist" that takes three parameters: a list of integers, a certain value, and a divisible value. The function should return a sublist of the given list containing elements that are greater than the certain value and divisible by the divisible value. The sublist should be sorted in descending order, contain no duplicate elements, and have a length between 5 and 15 elements. The solution should not use built-in functions such as filter(), sorted(), list comprehensions, or set(), and should have a time complexity of O(n) or less.
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