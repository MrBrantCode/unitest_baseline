"""
QUESTION:
Develop a function called `print_list` that takes an integer `N` as an argument. The function should return a list of consecutive numbers between 1 and `N` (inclusive) based on the following rules: 
- If `N` is odd, include only odd numbers in the list.
- If `N` is even, include only even numbers in the list.
Additionally, ensure that no three consecutive numbers in the list have a sum that is divisible by `N`. The function should be efficient in terms of time and space complexity.
"""

def print_list(N):
    # Initialize output list
    output = []

    # Check if N is odd
    if N % 2 == 1:
        # iterate through odd numbers from 1 to N
        for i in range(1, N + 1, 2):
            # Check if the sum of last 3 numbers is divisible by N
            if len(output) < 2 or (output[-1] + output[-2] + i) % N != 0:
                output.append(i)
    else:
        # iterate through even numbers from 2 to N
        for i in range(2, N + 1, 2):
            # Check if the sum of last 3 numbers is divisible by N
            if len(output) < 2 or (output[-1] + output[-2] + i) % N != 0:
                output.append(i)

    return output