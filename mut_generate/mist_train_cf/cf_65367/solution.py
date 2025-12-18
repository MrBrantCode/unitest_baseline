"""
QUESTION:
Create a function named `rearrange_array(arr)` that takes a list of integers as input and rearranges the elements such that every Fibonacci number is followed by a non-Fibonacci number. The function should return the rearranged list. The input list is not guaranteed to contain an equal number of Fibonacci and non-Fibonacci numbers.
"""

def is_fibonacci(n: int) -> bool:
    """This function will check if a number is Fibonacci number or not"""
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
    return y == n

def rearrange_array(arr: list) -> list:
    """This function will rearrange the array with Fibonacci number followed by a not Fibonacci number"""
    fib_list, not_fib_list = [], []
    for number in arr:
        if is_fibonacci(number) == True:
            fib_list.append(number)
        else:
            not_fib_list.append(number)

    rearranged_list = []
    while fib_list and not_fib_list:
        rearranged_list.append(fib_list.pop(0))
        rearranged_list.append(not_fib_list.pop(0))

    # put the remaining elements from two lists (if any) into the rearranged_list
    rearranged_list.extend(fib_list)
    rearranged_list.extend(not_fib_list)

    return rearranged_list