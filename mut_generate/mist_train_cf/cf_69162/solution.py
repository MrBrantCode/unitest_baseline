"""
QUESTION:
Create a function `square_root` that calculates the square root of a given number without using any built-in or library functions for square root calculation. Then, create another function `is_integer` to check if the calculated square root is an integer or not. Using these functions, process a list of numbers by replacing each number with its integer square root if the square root is an integer; otherwise, keep the original number in the list. Implement this for the list [121, 144, 169, 200].
"""

# Babylonian method
def square_root(n):
    x = n
    y = (x + 1) / 2
    
    while(y < x):
        x = y
        y = (x + (n / x)) / 2
        
    return x

def is_integer(num):
    if int(num) == num:
        return True
    return False

def entance(nums):
    new_list = []
    
    for number in nums:
        root = square_root(number)
        
        if is_integer(root):
            new_list.append(int(root))
        else:
            new_list.append(number)
            
    return new_list