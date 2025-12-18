"""
QUESTION:
This time Panda is doing great. He is good with mathematical problems. His teacher decided to puzzle him with summation problems.  

Consider the following definitions, assuming 1-based indexing:  

In the computation of B, one can choose +1 or -1 to multiply, for each arr[i].
Also, you are allowed to re-order the elements of arr, beforehand.

Help him find the maximum possible value of C.

Input Format
The first line contains T, the number of test cases.
Then N numbers follow.  

Output Format
Output the query of Panda in single line. Since the answer can be very large, mod it with 1000000007.  

Constraints

1 ≤ T ≤ 10
1 ≤ N ≤ 10^5
-10^9 ≤ arr[i] ≤ 10^9

Instructions
Write modular code  
Comment your code properly  

SAMPLE INPUT
1
4
1 2 3 4

SAMPLE OUTPUT
40
"""

def calculate_max_possible_value(arr, MOD=1000000007):
    """
    Calculate the maximum possible value of C for the given array arr.

    Parameters:
    arr (list of int): The array of numbers.
    MOD (int): The modulus value to be used for large numbers (default is 1000000007).

    Returns:
    int: The maximum possible value of C modulo MOD.
    """
    # Sort the array in descending order
    s = sorted(arr, reverse=True)
    
    # Calculate the first part of the sum
    summ = 0
    n = len(s)
    for i in range(n // 2):
        summ = (summ + s[i]) % MOD
    for i in range(n // 2, n):
        summ = (summ - s[i]) % MOD
    
    # If the length of the array is odd, handle the middle element
    if n % 2 != 0:
        summ = (summ + s[n // 2]) % MOD
        summ = (summ + s[n // 2]) % MOD
    
    # Calculate the second part of the sum
    summ2 = 0
    for e in s:
        summ2 = (summ2 + abs(e)) % MOD
    
    # Return the final result
    return (summ2 * summ) % MOD