"""
QUESTION:
Create a function named `get_remainders` that takes a list of integers as input and returns a list of remainders. The remainders are calculated by summing every two consecutive integers in the list and dividing the sum by the third integer in the sequence. The input list must not be null and must have a minimum length of three. If the input list is invalid, return an error message 'Error: Invalid Input'. The function should also handle and return an error message 'Error: Division by Zero' if a division by zero occurs. The input list can be up to size 10^5.
"""

def get_remainders(lst):
    # validate that the list is not null and has a minimum length of three
    if lst is None or len(lst) < 3:
        return 'Error: Invalid Input'

    else:
        # nest try-except block to handle potential ZeroDivisionError
        try:
            remainders = []
            for i in range(len(lst) - 2):
                # calculate remainder
                remainder = (lst[i] + lst[i+1]) % lst[i+2]
                remainders.append(remainder)
            return remainders

        except ZeroDivisionError:
            return 'Error: Division by Zero'