"""
QUESTION:
Rajesh has been challenge by his friend to find the number which have properties like,

Here take no 12 such that 
square of 12(12*12)=144
and 21 which is reverse of 12 have square(21*21)= 441 whose reverse is equal to  144

and now Rajesh is not getting any way how to solve the problem.So he makes a list of the number and need your help to tell whether a reverse number exist for that or not,

'T' test case and 'N' number.
    0<T>50
    0<N>10000

INPUT
The first line of input will be 'T' test case,follow by 'T' numbers

OUTPUT
If reverse number exist for that print that number or otherwise print No.

SAMPLE INPUT
2
12
11

SAMPLE OUTPUT
21
No

Explanation

You have to print the number if the reverse number exist otherwise print No
First number is 12 for this the reverse no is 21 whose square's reverse= square of 12
Second number is 11 for which no such number exist so print N0
"""

def find_reverse_number(n):
    # Convert the number to a string to find its reverse
    str_n = str(n)
    reverse_n = str_n[::-1]
    
    # Convert the reverse string back to an integer
    reverse_int = int(reverse_n)
    
    # Check if the original number is not equal to its reverse
    if str_n != reverse_n:
        # Calculate the squares of both numbers
        square_n = n ** 2
        square_reverse_n = reverse_int ** 2
        
        # Convert the squares to strings and reverse the string of the square of the reverse number
        str_square_n = str(square_n)
        str_square_reverse_n = str(square_reverse_n)
        reverse_str_square_reverse_n = str_square_reverse_n[::-1]
        
        # Check if the reversed square of the reverse number matches the square of the original number
        if str_square_n == reverse_str_square_reverse_n:
            return reverse_int
    
    # If no such reverse number exists, return "No"
    return "No"