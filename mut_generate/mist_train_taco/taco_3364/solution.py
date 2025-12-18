"""
QUESTION:
Find the count of numbers less than equal to N having exactly 9 divisors.
 
Example 1:
Input:
N = 100
Output:
2
Explanation:
The two numbers which have 
exactly 9 divisors are 36 and 100.
Example 2:
Input:
N = 1000
Output:
8 
Explanation:
The numbers are:
36 100 196 225 256 441 484 676
Your Task:  
You don't need to read input or print anything. Your task is to complete the function nineDivisors() which takes an integer N as an input parameter and returns the total number of elements from 1 to N inclusive, that have exactly 9 divisors.
Expected Time Complexity: O(sqrt(Nlog(logN)))
Expected Auxiliary Space:  O(sqrt(N))
 
Constraints:
1<=N<=10^{10}
"""

def count_numbers_with_nine_divisors(N):
    c = 0
    limit = int(N ** 0.5)
    prime = [i for i in range(limit + 1)]
    i = 2
    while i * i <= limit:
        if prime[i] == i:
            for j in range(i * i, limit + 1, i):
                if prime[j] == j:
                    prime[j] = i
        i += 1
    for i in range(2, limit + 1):
        p = prime[i]
        q = prime[i // prime[i]]
        if p * q == i and q != 1 and (p != q):
            c += 1
        elif prime[i] == i:
            if i ** 8 <= N:
                c += 1
    return c