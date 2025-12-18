"""
QUESTION:
A number can be called v-number if the sum of the lower half of the array is equal to the sum of the upper half of the array.

EXAMPLE:

if num = 1221

sum of lower half = 3

sum of upper half = 3

then it can be called as v-number

INPUT:
First line consists of number of test cases T. Next T lines consists of a number N.

OUTPUT:
For every number N print  "YES"(without quotes) if the number is V-number else "NO"(without quotes)

SAMPLE INPUT
2
12
1230

SAMPLE OUTPUT
NO
YES
"""

def is_v_number(num: int) -> str:
    # Convert the number to a list of its digits
    digits = list(map(int, str(num)))
    
    # Calculate the length of the list
    length = len(digits)
    
    # Calculate the sum of the lower half
    lower_half_sum = sum(digits[:length // 2])
    
    # Calculate the sum of the upper half
    upper_half_sum = sum(digits[length // 2:])
    
    # Check if the sums are equal
    if lower_half_sum == upper_half_sum:
        return "YES"
    else:
        return "NO"