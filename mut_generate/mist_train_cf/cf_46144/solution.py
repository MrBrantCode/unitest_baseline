"""
QUESTION:
Create a function `separate_square` that takes a list of numbers as input and returns a dictionary. The dictionary should contain two keys: 'even' and 'odd'. The values of these keys should be lists of squared numbers from the input list, grouped by whether they are even or odd. The function should ignore non-numeric values in the input list and handle potential exceptions.
"""

def separate_square(nums):
    result = {'even':[], 'odd':[]}
    
    for num in nums:
        try:
            num = int(num)
            square = num ** 2
            if square % 2 == 0:
                result['even'].append(square)
            else:
                result['odd'].append(square)
        except ValueError:
            print(f'{num} is not a valid integer.')
    
    return result