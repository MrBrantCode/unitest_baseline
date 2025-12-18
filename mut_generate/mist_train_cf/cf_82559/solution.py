"""
QUESTION:
Write a function `findElement(n)` that returns the nth element in a sequence where each element is the sum of the previous two even numbers, starting with 0 and 2. The function should run with a time complexity of O(n).
"""

def findElement(n):
    a = 0
    b = 2
    
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(3, n+1):
            number = a + b
            a = b
            b = number
        return number