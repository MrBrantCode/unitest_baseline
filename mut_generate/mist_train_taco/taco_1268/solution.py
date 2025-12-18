"""
QUESTION:
Given 6 numbers a,b,c,d,e,f. Find the last digit of (a^{b})*(c^{d})*(e^{f}).
 
Example 1:
Input:
a = 3 
b = 66 
c = 6 
d = 41 
e = 7 
f = 53
Output:
8
Explanation:
The last digit of the 
value obtained after 
solving the above 
equation is 8.
 
 
Example 2:
Input:
a = 1 
b = 1 
c = 1 
d = 1 
e = 1 
f = 1
Output:
1
Explanation:
The last digit of the 
value obtained after 
solving the above 
equation is 1.
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function theLastDigit() which takes 6 integers a, b, c, d, e, and f and returns the last digit of the value obtained from the equation.
 
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= a,b,c,d,e,f <= 10^{9}
"""

def calculate_last_digit(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    # Reduce the exponents modulo 4
    b %= 4
    d %= 4
    f %= 4
    
    # Handle the case where the reduced exponent is 0
    if b == 0:
        b = 4
    if d == 0:
        d = 4
    if f == 0:
        f = 4
    
    # Calculate the last digit of each term and multiply them
    last_digit = ((a % 10) ** b) * ((c % 10) ** d) * ((e % 10) ** f)
    
    # Return the last digit of the final product
    return last_digit % 10