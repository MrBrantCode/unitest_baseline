"""
QUESTION:
Write a function `example_function(a, b)` to calculate the sum of all integers in the range `[a, b]` with a time complexity of O(log n), where n is the difference between `a` and `b`. The function should take two integers `a` and `b` as input and return the calculated sum.
"""

def sum_of_range(a, b):
    total_sum = 0
    
    while a <= b:
        if a == b:
            total_sum += a
            break
            
        mid = (a + b) // 2
        total_sum += (b - a + 1) * (a + b) // 2
        
        b = mid
        a = mid + 1
    
    return total_sum