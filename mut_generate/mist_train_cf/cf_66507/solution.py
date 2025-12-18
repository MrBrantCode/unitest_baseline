"""
QUESTION:
Write a function `recursive_function(i, depth=0)` that performs a recursive countdown from `i` to `0` and adds the current value of `i` to a global variable `total` only when the recursion reaches the third depth level. The function should not take any other parameters besides `i` and `depth`, and it should use a base case to stop the recursion when `i` is less than or equal to `0`. The function should modify the global variable `total` and should not return any value.
"""

total = 0  

def recursive_function(i, depth=0):
    global total
    
    if i <= 0:
        return
    
    if depth == 2:
        total = total + i
    else:
        recursive_function(i-1, depth+1)
    recursive_function(i-1, depth)