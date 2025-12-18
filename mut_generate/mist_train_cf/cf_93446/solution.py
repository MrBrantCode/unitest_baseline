"""
QUESTION:
Create a recursive function named `print_list_elements` that prints the elements of a list without using loops. The function should take three parameters: a list of elements, a counter to keep track of the current index, and a limit to specify the maximum number of elements to print. The function should stop printing when the counter reaches the limit.
"""

def print_list_elements(lst, counter, limit):
    if counter == limit:
        return
    if counter < len(lst):
        print(lst[counter])
        print_list_elements(lst, counter+1, limit)