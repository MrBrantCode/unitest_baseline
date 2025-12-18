"""
QUESTION:
Create a function named `print_message` that takes one argument `num_times`. The function should print "Welcome to Tech World!" `num_times` times, followed by printing the same message `num_times` times in reverse order. Each message should be on a new line and preceded by its corresponding line number. If `num_times` is negative, the function should terminate immediately. The function should use a maximum of 3 variables and 1 loop, and it should run in O(n) time complexity.
"""

def print_message(num_times):
    if num_times < 0:
        return

    counter = 1
    reverse_counter = num_times
    iteration = 0
    while iteration < num_times * 2:
        if iteration < num_times:
            print(f"{counter}: Welcome to Tech World!")
            counter += 1
        else:
            print(f"{reverse_counter}: Welcome to Tech World!")
            reverse_counter -= 1
        iteration += 1