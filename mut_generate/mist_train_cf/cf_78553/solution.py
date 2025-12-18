"""
QUESTION:
Write a function `sum_every_third_reverse` that takes a list of integers as input and returns the sum of every 3rd element from the end of the list. If the input list is empty or contains less than 3 elements, return a corresponding error message. The function should also handle any potential exceptions.
"""

def sum_every_third_reverse(arr):
    try:
        if len(arr) == 0:
            print("The list is empty.")
            return
        if len(arr) < 3:
            print("The list is too short.")
            return
        new_arr = arr[::-1][2::3]
        return sum(new_arr)
    except Exception as e:
        print("An exception occurred: ", str(e))
        return None