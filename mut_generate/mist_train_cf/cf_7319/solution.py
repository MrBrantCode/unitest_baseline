"""
QUESTION:
Create a function named `softmax` that takes an array of numbers as input and returns the softmax values of the array. The function should not use any libraries or built-in functions for exponentiation or logarithms, and should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array. The solution should not use any control flow statements.
"""

def softmax(arr):
    # Find the maximum value in the array
    max_val = arr[0]
    for val in arr[1:]:
        if val > max_val:
            max_val = val

    # Subtract the maximum value from each element to avoid overflow
    shifted_arr = [val - max_val for val in arr]

    # Exponentiate each element
    exp_arr = []
    for val in shifted_arr:
        exp = 1
        for _ in range(abs(val)):
            if val > 0:
                exp *= 2
            else:
                exp /= 2
        exp_arr.append(exp)

    # Sum all the exponentiated values
    sum_exp = 0
    for val in exp_arr:
        sum_exp += val

    # Divide each exponentiated value by the sum
    softmax_arr = [val / sum_exp for val in exp_arr]

    return softmax_arr