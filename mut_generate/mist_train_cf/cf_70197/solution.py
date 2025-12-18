"""
QUESTION:
Create a function `merge_elements(l: list)` that takes a list of elements as input, which can be integers, floats, or strings. The function should return a single string that combines all elements from the input list, handling each data type correctly. The function must not use any type-casting methods or built-in functions that convert data types.
"""

def merge_elements(l: list):
    result = ""
    for element in l:
        if isinstance(element,int):
            digit = ""
            while element > 0:
                digit = chr((element%10) + ord('0')) + digit
                element //= 10
            result += digit
        elif isinstance(element,float):
            left = int(element)
            right = element - left
            result += merge_elements([left])
            result += '.'
            right = int(right * 10**6)
            result += merge_elements([right])
        else:
            result += element 
    return result