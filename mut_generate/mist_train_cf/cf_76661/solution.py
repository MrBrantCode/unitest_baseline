"""
QUESTION:
Create a function my_func that takes three lists of integers x, y, and z as parameters and returns a new list containing only the unique maximum integer(s) from each list. If a list is empty, consider its maximum to be 0. Implement the solution without using built-in Python functions such as max(). The function should handle large lists efficiently.
"""

def entrance(x, y, z):
    lists = [x, y, z]
    result = []
    
    for lis in lists:
        if not lis:
            result.append(0)
        else:
            max_num = -10**18  
            for num in lis:
                max_num = max(max_num, num)
            result.append(max_num)
    
    result = list(dict.fromkeys(result))
    return result