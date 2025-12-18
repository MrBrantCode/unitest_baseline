"""
QUESTION:
Regional Students's are taught to add multi-digit numbers from right-to-left one digit at a time.
Many find the "carry" operation - in which 1 is carried from one digit position
to be added to the next - to be a significant challenge.  Your job is to
count the number of carry operations for each of addition problem so that educators may assess their difficulty.

For the input first line contains n number of records which is less then 1000. And then each line contains two numbers with spacing between them as shown in sample. 

SAMPLE INPUT
3
123 456
555 555
123 594

SAMPLE OUTPUT
No carry operation
3 carry operations
1 carry operation

Explanation

EXAMPLE 1:-

when the digits are added then there is no carry found as 3+6=9,2+5=7 and 1+4=5.

EXAMPLE 2:-

when the digits are added then carry is generated as 5+5 =10 so carry is found 3 times.

EXAMPLE 3:-

when the digits 9 and 2 are added only then carry is found so 1 time only.
"""

def count_carry_operations(a: str, b: str) -> tuple:
    # Convert the string inputs to lists of integers
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    
    # Pad the shorter number with leading zeros
    while len(a) < len(b):
        a = [0] + a
    while len(b) < len(a):
        b = [0] + b
    
    carry_count = 0
    carry = 0
    
    # Iterate from the last digit to the first
    for i in range(len(a) - 1, -1, -1):
        if a[i] + b[i] + carry >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
    
    # Prepare the carry message
    if carry_count == 0:
        carry_message = "No carry operation"
    elif carry_count == 1:
        carry_message = "1 carry operation"
    else:
        carry_message = f"{carry_count} carry operations"
    
    return carry_count, carry_message