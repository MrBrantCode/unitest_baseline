"""
QUESTION:
A pronic number is a number which is the product of two consecutive integers. Find all Pronic Numbers less than  or equal to the given integer N.
The first few Pronic numbers are: 0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132 and so on.
Example 1:
Input:
N = 6
Output:
0 2 6
Explanation:
0 is the product of 0 and 1.
2 is the product of 1 and 2.
6 is the product of 2 and 3.
Example 2:
Input:
N = 56
Output:
0 2 6 12 20 30 42 56
Explanation:
0 is the product of 0 and 1.
2 is the product of 1 and 2.
6 is the product of 2 and 3.
12 is the product of 3 and 4.
and so on.
Your Task:  
You don't need to read input. Your task is to complete the function pronicNumbers() which takes an integer N as input parameter and returns a list of integers. 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints: 
1 <= N <= 10^{5}
"""

def find_pronic_numbers(N: int) -> list[int]:
    i = 0
    pronic_numbers = []
    while True:
        pronic = i * (i + 1)
        if pronic > N:
            break
        pronic_numbers.append(pronic)
        i += 1
    return pronic_numbers