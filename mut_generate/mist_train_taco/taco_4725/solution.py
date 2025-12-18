"""
QUESTION:
Given an integer n and a permutation of numbers 1, 2 ... , n-1, n write a program to print the permutation that lexicographically precedes the given input permutation. If the given permutation is the lexicographically least permutation, then print the input permutation itself. 

Input Format: 

First line is the test cases and second line contains value of integer n: 1 ≤ n ≤ 1,000,000 
third line is a space separated list of integers 1 2 ... n permuted in some random order 

Output Format: 

Output a single line containing a space separated list of integers which is the lexicographically preceding permutation of the input permutation.

SAMPLE INPUT
1
3
1 3 2

SAMPLE OUTPUT
1 2 3
"""

def find_lexicographically_preceding_permutation(n, permutation):
    b = []
    flag = 0
    
    for x in range(n-1, 0, -1):
        b = permutation[:x-1]
        if permutation[x] < permutation[x-1]:
            for y in range(n-1, x-1, -1):
                if permutation[x-1] > permutation[y]:
                    b.append(permutation[y])
                    flag = 1
                    c = permutation[x-1:]
                    del(c[y-x+1])
                    c.sort()
                    c.reverse()
                    b = b + c
                if flag == 1:
                    break
        if flag == 1:
            break
    
    if flag == 0:
        return permutation
    else:
        return b