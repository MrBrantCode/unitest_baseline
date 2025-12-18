"""
QUESTION:
A tutorial for this problem is now available on our blog. Click here to read it.  

You are asked to calculate factorials of some small positive integers.

------ Input ------ 

An integer t, 1≤t≤100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1≤n≤100.

------ Output ------ 

For each integer n given at input, display a line with the value of n!

----- Sample Input 1 ------ 
4
1
2
5
3
----- Sample Output 1 ------ 
1
2
120
6
"""

def calculate_factorials(test_cases):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    results = []
    for num in test_cases:
        results.append(factorial(num))
    
    return results