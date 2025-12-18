"""
QUESTION:
Implement a function named `sort_tuples` that takes a list of tuples as input, where each tuple contains two integers and one string. The function should sort the list in ascending order by the first integer, then in descending order by the second integer, and finally in descending order by the length of the string. The function must not use Python's built-in `sort` function or any similar library functions, and instead implement its own sorting algorithm.
"""

def sort_tuples(lst):
    # Bubble sort
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            # If first integer of list[j] is greater than the first integer of list[j+1]
            if lst[j][0] > lst[j+1][0]:
                # Swap list[j] and list[j+1]
                lst[j], lst[j+1] = lst[j+1], lst[j]
            # If first integer is same
            elif lst[j][0] == lst[j+1][0]:
                # Then compare the second integer
                if lst[j][1] < lst[j+1][1]:
                    # Swap
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                # If second integer is same
                elif lst[j][1] == lst[j+1][1]:
                    # Then compare lengths of string
                    if len(lst[j][2]) < len(lst[j+1][2]):
                        # Swap
                        lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst