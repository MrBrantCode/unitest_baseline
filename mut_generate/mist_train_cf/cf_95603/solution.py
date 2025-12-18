"""
QUESTION:
Write a Python function `same_frequency(num1, num2)` that takes two integers `num1` and `num2` and returns True if they have the same frequency of digits, False otherwise. The function should not convert the numbers to strings or use any built-in functions for counting the frequency of digits.
"""

def same_frequency(num1, num2):
    freq1 = {}
    freq2 = {}
    temp1 = num1
    temp2 = num2
    
    while temp1 != 0 or temp2 != 0:
        digit1 = temp1 % 10
        digit2 = temp2 % 10
        temp1 //= 10
        temp2 //= 10
        
        if freq1.get(digit1) is None:
            freq1[digit1] = 1
        else:
            freq1[digit1] += 1
        
        if freq2.get(digit2) is None:
            freq2[digit2] = 1
        else:
            freq2[digit2] += 1
    
    if temp1 != 0 or temp2 != 0:
        return False
    
    return freq1 == freq2