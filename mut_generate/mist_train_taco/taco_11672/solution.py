"""
QUESTION:
Big P is fairly good in mathematics.
His teacher has asked him to add two numbers.
Now , Big P has a problem that he sometimes writes a '6' as a '5' and vice versa.
Given two numbers, A and B, calculate the minimum and the maximum sum Big P could possibly get. 

Input:
The first and only line of input contains positive integers A and B . 

Output:
In single line of output, print two space separated integers, minimum and maximum sum Big P could get. 

Constraints:

1 ≤ A,B ≤ 1000000

SAMPLE INPUT
11 25

SAMPLE OUTPUT
36 37
"""

def calculate_sum_variations(A: int, B: int) -> tuple:
    def convert_number(num, to_min=True):
        str_num = str(num)
        converted_num = ""
        for char in str_num:
            if char == '6' and to_min:
                converted_num += '5'
            elif char == '5' and not to_min:
                converted_num += '6'
            else:
                converted_num += char
        return int(converted_num)

    min_A = convert_number(A, to_min=True)
    min_B = convert_number(B, to_min=True)
    max_A = convert_number(A, to_min=False)
    max_B = convert_number(B, to_min=False)

    min_sum = min_A + min_B
    max_sum = max_A + max_B

    return (min_sum, max_sum)