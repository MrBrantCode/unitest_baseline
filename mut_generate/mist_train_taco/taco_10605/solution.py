"""
QUESTION:
Sumit had borrowed money from many of his batch mates and today he has decided to pay them  because he has got lottery today.

The amount of lottery is very large. So to count the money he decided to write the amount in Indian system first.

In the Indian system the rightmost comma is placed after three rightmost digits, and then a comma is placed after every two digits from the right.

He has asked you to write code for that.

Input

First line contains T number of test cases.

Each test case contain the amount . The amount is in string whose maximum length is 10^4.

Output

Print T lines of output each containing the amount in Indian way of writing with commas.

If amount is less than or equal to 3 digits, then do not put any commas.

Constraints

1 ≤ T ≤200

1 ≤ |amount| ≤10^4

SAMPLE INPUT
3
12345
54321
125634

SAMPLE OUTPUT
12,345
54,321
1,25,634
"""

def format_indian_currency(amount: str) -> str:
    A, l, flag, x = '', len(amount) - 1, 0, 1
    while l >= 0:
        if flag > 0:
            if x == 2:
                A += amount[l]
                A += ','
                x = 1
            else:
                A += amount[l]
                x += 1
        else:
            if x == 3:
                flag = 1
                x = 1
                A += amount[l]
                A += ','
            else:
                A += amount[l]
                x += 1
        l -= 1
    if A[len(A) - 1] == ',':
        formatted_amount = A[:len(A) - 1][::-1]
    else:
        formatted_amount = A[::-1]
    return formatted_amount