"""
QUESTION:
Write a function `five_div_seq(n)` that calculates the frequency of the numeral 5 in integers below a specific threshold 'n'. The integers must meet the following conditions: 
- be divisible by 9 or 14, 
- have at least 4 distinct digits, 
- include the digit 2, and 
- be part of a descending arithmetic sequence with a uniform even interval of 2.
"""

def five_div_seq(n: int):
    count = 0
    for i in range(n-1, 999, -2): 
        str_i = str(i) 
        if len(set(str_i)) >= 4 and '2' in str_i: 
            if i % 9 == 0 or i % 14 == 0: 
                count += str_i.count('5') 
    return count