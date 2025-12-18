"""
QUESTION:
Create a function called "initialize_list" that takes a parameter "start" and returns a list containing consecutive numbers from "start" to "start+99". The function should use a loop to populate the list.
"""

def initialize_list(start):
    my_list = []
    for num in range(start, start+100):
        my_list.append(num)
    return my_list