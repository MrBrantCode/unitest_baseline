"""
QUESTION:
Create a function called "modified_array" that takes an integer n as input and returns an array of numbers from 0 to n, following these rules: 
- If n is negative, return an empty array. 
- If n is 0, return an array with only the number 0. 
- Exclude the number 3 from the array. 
- Double the number 5 before including it in the array. 
- For numbers that are divisible by 3, include their square root rounded to the nearest whole number instead of the number itself. 
- Make any negative numbers in the array positive before returning the final array.
"""

import math

def modified_array(n):
    if n < 0:
        return []
    
    result = []
    for i in range(n+1):
        if i == 3:
            continue
        elif i == 5:
            result.append(2 * i)
        elif i % 3 == 0:
            result.append(round(math.sqrt(i)))
        else:
            result.append(abs(i))
    
    return result