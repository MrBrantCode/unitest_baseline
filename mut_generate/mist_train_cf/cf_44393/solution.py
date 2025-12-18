"""
QUESTION:
Write a function `find_number` that takes two optional parameters `ratio_min` and `ratio_max` with default values of 0.52 and 0.58 respectively. The function should find a two-digit number where the digit in the tens place is 4 less than seven times the digit in the ones place. When the digits are switched, the new number should be between `ratio_min` and `ratio_max` times the original number. If such a number exists, return it; otherwise, return "No solution found".
"""

def find_number(ratio_min=0.52, ratio_max=0.58):
    for i in range(10,100):
        tens = i // 10 
        ones = i % 10 
        if tens == 7 * ones - 4:        
            switched = ones * 10 + tens 
            ratio = switched / i       
            if ratio_min <= ratio <= ratio_max: 
                return i
    return "No solution found"