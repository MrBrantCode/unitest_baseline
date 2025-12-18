"""
QUESTION:
Design a function `Heptagonal(n)` to calculate the nth heptagonal figure number. The function should be able to handle non-positive integers and inputs exceeding 2000. It should also compute the cumulative sum and product of all heptagonal figure numbers up to the nth number.

The function should be able to handle multiple queries efficiently, avoiding recalculations of previously computed heptagonal figure numbers. It should also accept numerical ranges and arrays of numbers as input and produce the corresponding sequence of heptagonal figure numbers.

The function should provide meaningful error messages for erroneous inputs, such as strings or negative numbers. It should be optimized for space efficiency and capable of handling large inputs without causing a stack overflow error.

Implement the function using dynamic programming techniques and provide the cumulative sum and product functions. Also, include a safe version of the function that handles erroneous inputs.

Additionally, explain how to modify the function to handle parallel processing for multiple inputs, optimize it for space efficiency, and extend it to calculate other types of polygonal numbers, such as octagonal or decagonal numbers.
"""

def Heptagonal(n):
    dp = [-1]*2005  # Initialize a dp array with -1
    if n<=0:
        return 0
    if dp[n]!=-1:
        return dp[n]
    dp[n] = n*(5*n-3)//2
    return dp[n]