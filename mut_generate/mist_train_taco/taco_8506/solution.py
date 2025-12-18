"""
QUESTION:
For any two given positive integers p and q, find (if present) the leftmost digit in the number obtained by computing the exponent p^{q}  i.e. p raised to the power q, such that it is a divisor of p^{q}.
Note: p^{q}^{ }may be a very huge number, so if the number of digits in p^{q} is greater than 18, you need to extract the first 10 digits of the result and  check if any digit of that number divides the number.
Example 1:
Input: p = 1, q = 1
Output: 1 
Explanation: 1 raised to the power 1 gives 1, 
which is a divisor of itself i.e. 1.  
Example 2:
Input: p = 5, q = 2
Output: 5
Explanation: The exponent 5 raised to the power 2 
gives 25, wherein leftmost digit 2, does not 
divide 25 but 5 does. Hence output is 5. 
Your Task:  
You dont need to read input or print anything. Complete the function leftMostDiv() which takes p and q as input parameter and returns the left-most digit in the number p^{q} which is a divisor of p^{q}. If no such digit exists, returns -1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 <= p , q <=50
"""

def find_leftmost_divisor(p: int, q: int) -> int:
    # Calculate the exponent
    e = p ** q
    
    # If the number of digits in e is greater than 18, extract the first 10 digits
    if len(str(e)) > 18:
        e = int(str(e)[:10])
    
    # Convert the result to string to iterate over each digit
    e_str = str(e)
    
    # Iterate over each digit from left to right
    for digit in e_str:
        # Skip '0' as it cannot be a divisor
        if digit != '0':
            # Check if the digit is a divisor of the original number
            if e % int(digit) == 0:
                return int(digit)
    
    # If no such digit is found, return -1
    return -1