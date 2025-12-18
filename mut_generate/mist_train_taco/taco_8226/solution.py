"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Trans bought a calculator at creatnx's store. Unfortunately, it is fake. It has many bugs. One of them is adding two numbers without carrying. Example expression: 12 + 9 will have result 11 in his calculator. Given an expression in the form a + b, please output result from that calculator.
 
------ Input ------ 

The first line contains an integer T denote the number of test cases. Each test case contains two integers a, b in a single line.
 
------ Output ------ 

Each test case, print answer in a single line.
 
------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ a, b ≤ 10^{9}$

Subtasks:

$Subtask #1 (30 points): 1 ≤ a, b ≤ 9$
$Subtask #2 (70 points): original constrains$

----- Sample Input 1 ------ 
2

12 9

25 25
----- Sample Output 1 ------ 
11

40
"""

import math

def fake_calculator_sum(a, b):
    multiplier = 1
    result = 0
    while a or b:
        bit_sum = (a % 10) + (b % 10)
        bit_sum %= 10
        result += bit_sum * multiplier
        a = math.floor(a / 10)
        b = math.floor(b / 10)
        multiplier *= 10
    return result