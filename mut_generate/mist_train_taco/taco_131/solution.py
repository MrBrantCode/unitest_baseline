"""
QUESTION:
-----General Statement:-----
Read a number in scientific notation and output its equivalent decimal value.

-----Input:-----
All data is on a single line. The first integer indicates how many pairs of numbers follow. The first of each pair is A, the base number, and the second is E, the power of 10.

-----Output:-----
Round each answer to 2 decimal places. Trailing zeros to the right of the decimal point are required. A leading zero to the left of the decimal point is not required.
The output is to be formatted exactly like that for the sample output given below.

-----Assumptions:-----
E is in the range –10 .. 10. A is 1 or larger but less than 10.
Discussion: 
If A = 3.926 and E = 4, the number represented is 3.926 X 104 or 39260, which is 39260.00 when rounded to 2 decimal places.

-----Sample Input:-----
4 4.296 3 3.8 -2 1.8 2 2.8678 1

-----Sample Output:-----
4296.00
0.04
180.00
28.68
"""

def convert_scientific_notation_to_decimal(input_data):
    n = int(input_data[0])
    arr = []
    i = 1
    while i < len(input_data):
        arr.append(float(input_data[i]))
        i += 1
        arr.append(int(input_data[i]))
        i += 1
    
    ans = []
    i = 0
    while i < len(arr):
        base = arr[i]
        i += 1
        exponent = arr[i]
        i += 1
        decimal_value = base * (10 ** exponent)
        ans.append('{:.2f}'.format(decimal_value))
    
    return ans