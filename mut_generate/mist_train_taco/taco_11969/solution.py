"""
QUESTION:
Decimal numbers are a common notation system currently in use and use ten symbols 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 to represent all numbers.

Binary numbers are a popular notation in the computer world and use two symbols, 0 and 1, to represent all numbers.

Only the four numbers 0, 1, 2, and 3 are used in quaternary numbers. In quaternary numbers, when the number is incremented from 0, it will be carried to the next digit when it reaches 4. Therefore, the decimal number 4 is carried to the expression "10".

Decimal | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | ...
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |- ---
Binary | 0 | 1 | 10 | 11 | 100 | 101 | 110 | 111 | 1000 | 101 | 1010 | ...
Quadrant | 0 | 1 | 2 | 3 | 10 | 11 | 12 | 13 | 20 | 21 | 22 | ...



In Hawaii, fish and taro were counted between fingers in the old days, so it seems that they used quaternary numbers instead of decimal numbers.

Create a program that converts the integer n input in decimal to decimal and outputs it.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of -1. One integer n (0 ≤ n ≤ 1000000) is given on one row for each dataset.

The number of datasets does not exceed 2000.

Output

The result of conversion to quaternary number for each input data set is output on one line.

Example

Input

7
4
0
12
10
10000
-1


Output

13
10
0
30
22
2130100
"""

def decimal_to_quaternary(n: int) -> str:
    if n < 4:
        return str(n)
    
    b = bin(n)[2:]  # Convert decimal to binary and remove the '0b' prefix
    bb = [b[i:i + 2] for i in range(len(b) - 2, -1, -2)]  # Split binary string into chunks of 2
    
    if len(b) % 2 != 0:
        bb.append(b[0])  # If the binary length is odd, append the first digit
    
    ans = []
    for t in bb:
        tmp = 0
        for (i, v) in enumerate(t[::-1]):
            tmp += pow(2, i) * int(v)  # Convert each chunk to quaternary
        ans.append(tmp)
    
    return ''.join(map(str, ans[::-1]))  # Join the quaternary digits in reverse order