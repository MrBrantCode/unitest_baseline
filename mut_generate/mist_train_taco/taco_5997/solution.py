"""
QUESTION:
Given an array A. Is there any subset of array A in which if we do AND of all elements of that subset then output should be in power of two (for example : 1,2,4,8,16 and so on ).    

Input: 
First line contains number of test cases T. Each test first line contains N size of array A and next line contains N space separated integers.  

Output: 
For each test case print YES if there is any subset of array A in which if we do AND of all elements of that subset then output should be in power of two else print NO.  

Constraints: 
1 ≤ T ≤ 1000 
1 ≤ N ≤ 200 
0 ≤ Ai ≤ 10^9

SAMPLE INPUT
2
3
1 2 3
2
10 20SAMPLE OUTPUT
YES
NO
"""

from itertools import combinations

def has_power_of_two_subset(A, N):
    # Check if any single element is a power of two
    if any(bin(i).count("1") == 1 for i in A):
        return "YES"
    
    # Check pairs of elements
    for i, j in combinations(A, 2):
        if bin(i & j).count("1") == 1:
            return "YES"
    
    # Check triplets of elements if the array has at least 3 elements
    if N >= 3:
        for i, j, k in combinations(A, 3):
            if bin(i & j & k).count("1") == 1:
                return "YES"
    
    return "NO"