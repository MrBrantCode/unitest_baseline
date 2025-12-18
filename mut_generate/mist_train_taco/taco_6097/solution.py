"""
QUESTION:
Programmer Deepak has created a program which calculates magical number as 2^n * 3^n * 5^n where "n" is an integer.

Now he wants to find the magical number which is just greater than the input. Help him in finding it.

NOTE :  a^b denotes a raised to power b.

Input : 
456

NOTE : You do not need to create a program for this problem you have to write your answers of small input and large input in given code snippet
To see how to submit solution please check this link

SAMPLE INPUT
28

SAMPLE OUTPUT
30
"""

def find_next_magical_number(input_number: int) -> int:
    n = 1
    while True:
        magical_number = (2 ** n) * (3 ** n) * (5 ** n)
        if magical_number > input_number:
            return magical_number
        n += 1