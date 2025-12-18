"""
QUESTION:
Is the MRP of my new shoes exclusive or inclusive of taxes?

-----Input:-----
- First line will contain an integer $P$

-----Output:-----
For each testcase, print either 'Inclusive' or 'Exclusive' without quotes.

-----Constraints-----
- $100 \leq P \leq 999$

-----Sample Input 1:-----
123

-----Sample Output 1:-----
Exclusive

-----Sample Input 2:-----
111

-----Sample Output 2:-----
Inclusive
"""

def determine_tax_inclusion(P: int) -> str:
    # Convert the integer to a string to iterate over its digits
    n = str(P)
    ans = 0
    
    # XOR each digit of the number
    for i in n:
        ans = ans ^ int(i)
    
    # Determine if the result is 'Inclusive' or 'Exclusive'
    if ans:
        return 'Inclusive'
    else:
        return 'Exclusive'