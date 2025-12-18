"""
QUESTION:
You are given a number N, you have to represent this number as the sum of the minimum number of possible pseudo-binary numbers. A number is said to be a pseudo-binary number if its decimal number consists of only two digits (0 and 1).
Few examples of pseudo-binary numbers are 0, 1, 10, 11, 101, 110 etc 
Example:
Input:
N = 31
Output:
11 10 10
Explanation: 
31 can be represented as the sum of
minimum 3 pseudo-binary numbers as 11+10+10.
Example:
Input:
N = 12
Output:
11 1
Explanation: 
12 can be represented as sum of
minimum 2 psuedo-binary numbers as 11+1.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minimumPseudoBinary() which takes an integer N as an input parameter and return the list of the minimum number of pseudo-binary numbers in non-increasing order that sums up to N.
Expected Time Complexity: O(NLogN)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{6}
"""

def minimum_pseudo_binary(N):
    result = []
    while N != 0:
        m = str(N)
        for i in m:
            if int(i) > 1:
                m = m.replace(i, '1')
        result.append(int(m))
        N = N - int(m)
    return result