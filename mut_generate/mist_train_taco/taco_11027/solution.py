"""
QUESTION:
Chef is good at making pancakes. Generally he gets requests to serve N pancakes at once.
He serves them in the form of a stack.
A pancake can be treated as a circular disk with some radius.
Chef needs to take care that when he places a pancake on the top of the stack the radius of the pancake should not exceed the radius of the largest pancake in the stack by more than 1. 
Additionally all radii should be positive integers, and the bottom most pancake should have its radius as 1.
Chef wants you to find out in how many ways can he create a stack containing N pancakes.
Input
First line of the input contains T (T <= 1000) denoting the number of test cases.
T lines follow each containing a single integer N (1 <= N <= 1000) denoting the size of the required stack.
Output
For each case the output should be a single integer representing the number of ways a stack of size N can be created. As the answer can be large print it modulo 1000000007.
Example
Input
2
1
2

Output
1
2
"""

def count_valid_pancake_stacks(N: int) -> int:
    MOD = 1000000007
    
    # Precompute Bell numbers up to 1000
    bell_numbers = [[1]]
    for c in range(1, 1001):
        row = [bell_numbers[-1][-1]]
        for b in bell_numbers[-1]:
            row.append((row[-1] + b) % MOD)
        bell_numbers.append(row)
    
    # The number of ways to create a stack of size N is the Bell number at index N
    return bell_numbers[N][0]