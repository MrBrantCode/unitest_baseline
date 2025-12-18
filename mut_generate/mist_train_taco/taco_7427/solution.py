"""
QUESTION:
A digit string is good if the digits (0-indexed) at even indices are even and digits at odd indices are prime ( 2 , 3 , 5 or 7 ).
	For example, "4562" is good because the digits (4 and 6) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good.
Given an integer N , return the total number of good digit strings of length N.
Since the answer may be too large, return it modulo 10^{9} + 7.
Note : A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
 
Example 1:
Input:
N = 1
Output:
5
Explanation:
The good digit string of length of 1 are "0" , "2" , "4" ,"6" and "8".
Example 2:
Input:
N = 3
Output:
100
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countGoodNumbers() which takes an integer N as inputs returns the total number of good digit strings of length N . As this result can be very large return the result under modulo 10^{9}+7.
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{1}^{5}
"""

def powerOf(n, pow, modValue):
    result = 1
    while pow > 0:
        if pow & 1:
            result = result * n % modValue
        n = n * n % modValue
        pow >>= 1
    return result

def countGoodNumbers(N):
    modValue = 1000000007
    isOdd = N & 1 != 0
    result = powerOf(20, N >> 1, modValue)
    if isOdd:
        result = result * 5 % modValue
    return result