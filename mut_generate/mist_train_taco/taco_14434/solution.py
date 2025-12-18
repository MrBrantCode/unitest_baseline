"""
QUESTION:
Geek lost the password of his super locker. He remembers the number of digits N as well as the sum S of all the digits of his password. He know that his password is the largest number of N digits that can be made with given sum S. As he is busy doing his homework, help him retrieving his password.
Example 1:
Input:
N = 5, S = 12
Output:
93000
Explanation:
Sum of elements is 12. Largest possible 
5 digit number is 93000 with sum 12.
Example 2:
Input:
N = 3, S = 29
Output:
-1
Explanation:
There is no such three digit number 
whose sum is 29.
Your Task : 
You don't need to read input or print anything. Your task is to complete the function largestNumber() which takes 2 integers N and S as input parameters and returns the password in the form of string, else return "-1" in the form of string.
Constraints:
1 ≤ N ≤ 10^{4}
0 ≤ S ≤ 9*10^{4}
Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)
"""

def largest_number(N, S):
    # Initialize a list to hold the digits of the number
    digits = [0] * N
    
    # Try to fill the digits with the largest possible values
    for i in range(N):
        if 9 <= S:
            digits[i] = 9
            S -= 9
        else:
            digits[i] = S
            S = 0
    
    # If the sum of the digits is not equal to the original sum, return -1
    if sum(digits) != S:
        return "-1"
    
    # Convert the list of digits to a string and return
    return ''.join(map(str, digits))