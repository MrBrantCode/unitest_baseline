"""
QUESTION:
Create a function `sum_odd_following` that takes a list of integers as input and returns a dictionary. The dictionary should contain key-value pairs where the keys are even integers from the input list and the values are the sum of all odd integers that come after the corresponding even integer in the input list. Only include even integers in the dictionary if they have at least one odd integer following them in the input list.
"""

def sum_odd_following(numbers):
    result = {}
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            odd_sum = sum(num for num in numbers[i+1:] if num % 2 != 0)
            if odd_sum != 0:
                result[numbers[i]] = odd_sum
    return result