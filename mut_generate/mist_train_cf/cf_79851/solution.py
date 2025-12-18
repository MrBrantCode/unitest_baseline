"""
QUESTION:
Write a function `print_custom_msg` that takes two parameters: an integer `iteration` and a string `msg`. Using recursion, print the message along with the iteration number, 10 times. In the 5th iteration, the message should be reversed. The function should not take any other input or produce any output other than the recursive calls.
"""

def print_custom_msg(iteration, msg):
    if iteration > 10:
        return
    else:
        if iteration == 5:
            print(f"Iteration {iteration}: {msg[::-1]}")
        else:
            print(f"Iteration {iteration}: {msg}")
        print_custom_msg(iteration + 1, msg)