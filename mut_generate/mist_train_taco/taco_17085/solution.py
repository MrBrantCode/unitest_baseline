"""
QUESTION:
You are given a binary string s of length n. You have to perform binary addition of the string with '1'.
 
Example 1:
Input: 
n = 4
s = 1010
Output: 1011
Explaination: 
The decimal equivalent of given s is 10, 
Adding 1 gives 11, its binary representation
is 1011.
 
Example 2:
Input: 
n = 3
s = 111
Output: 1000
Explaination: The given number is 7. 
Now 7+1 = 8, whose binary representation 
is 1000.
 
Your Task:
You do not need to read input or print anyhthing. Your task is to complete the function binaryAdd() which takes n and s as input parameters and returns the resultant binary string after adding 1 with s.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ n ≤ 10000
"""

def binary_add_one(s: str) -> str:
    # Reverse the binary string to process from the least significant bit
    s = s[::-1]
    
    # Convert the binary string to its decimal equivalent
    val = 0
    for i in range(len(s)):
        val += 2 ** i * int(s[i])
    
    # Add 1 to the decimal value
    val += 1
    
    # Convert the decimal value back to a binary string, excluding the '0b' prefix
    binn = bin(val)[2:]
    
    # Calculate the difference in length between the original binary string and the new one
    diff = len(s) - len(binn)
    
    # If the new binary string is shorter, pad it with leading zeros
    if diff > 0:
        binn = '0' * diff + binn
    
    return binn