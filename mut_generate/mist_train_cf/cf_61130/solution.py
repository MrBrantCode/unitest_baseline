"""
QUESTION:
Write a function `choose_num(x, y, z, n)` that takes four positive integers `x`, `y`, `z`, and `n` as input. The function should return the `n`th largest even number in the range `[x, y]` (inclusive of both `x` and `y`) that can be divided by `z`. If no such number exists in the specified range, the function should return -1.
"""

def choose_num(x, y, z, n):
    # Initialize an empty list to store the even numbers divisible by z
    chosen_num_list = []

    # If y is less than x, switch their values. This ensures x is the start of the range and y is the end.
    if y < x:
        x, y = y, x

    # Scan every number in the range [x, y]
    for num in range(x, y+1):
        # If num is even and divisible by z, add it to the list
        if num % 2 == 0 and num % z == 0:
            chosen_num_list.append(num)

    # Sort the list in descending order to get the nth largest number at index n-1
    chosen_num_list.sort(reverse=True)

    # If the length of the list is less than n (no nth largest number), return -1
    if len(chosen_num_list) < n:
        return -1
    else:
        return chosen_num_list[n-1]