"""
QUESTION:
Subodhians are taught to add multi-digit numbers from right-to-left one digit at a time.
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

def count_carry_operations(num1: str, num2: str) -> int:
    # Reverse the digits of both numbers
    x = list(map(int, num1))[::-1]
    y = list(map(int, num2))[::-1]
    
    carry = 0
    ans = 0
    
    # Iterate through the digits from right to left
    for i in range(max(len(x), len(y))):
        digit1 = x[i] if i < len(x) else 0
        digit2 = y[i] if i < len(y) else 0
        
        if digit1 + digit2 + carry > 9:
            carry = 1
            ans += 1
        else:
            carry = 0
    
    return ans