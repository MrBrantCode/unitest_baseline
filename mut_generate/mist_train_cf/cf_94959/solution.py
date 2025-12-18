"""
QUESTION:
Create a function named replace_odd_numbers that takes an array of integers as input. Replace each odd number in the array with the sum of its adjacent even numbers. If there are no adjacent even numbers or the sum of adjacent even numbers is 0, replace the odd number with -1. If one of the adjacent numbers is even, replace the odd number with the product of the odd number and the adjacent even number. The function should return the modified array.
"""

def replace_odd_numbers(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:  
            result.append(arr[i])
        else:
            if i == 0 or i == len(arr) - 1:
                result.append(-1)  
            else:
                prev = arr[i - 1]
                next = arr[i + 1]
                if prev % 2 == 0 and next % 2 == 0:
                    result.append(prev + next)  
                elif prev % 2 == 0 or next % 2 == 0:
                    result.append(arr[i] * (prev if prev % 2 == 0 else next))  
                else:
                    result.append(-1)  
    return result