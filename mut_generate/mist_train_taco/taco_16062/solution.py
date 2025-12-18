"""
QUESTION:
The Indian bank issues coins in 4 denominations, ₹1, ₹2, ₹5 and ₹10. 

Given a limited supply of each of the above denominations, in how many ways can you sum them up to a total of ₹N?

Input Format 

The first line contains an integer T (number of testcases). 
Each testcase contains 2 lines. The first line contains integer N (sum to be achieved) 

A, B, C and D in the next line, each representing the number of ₹1, ₹2, ₹5 and ₹10 coins respectively. 

Output Format 

Output the number of ways in which we can achieve the sum N.   

Constraints 

1 <= T <= 150 

1 <= N <= 1000 

1 <= A <= 10000 

1 <= B,C,D <= 1000  

Sample Input  

2
15
2 3 1 1
12
2 2 1 1

Sample Output

2
2

Explanation 

In the first case we need to find the different ways to total to 15. 
We can use one ₹10 coin and one ₹5 coin  or one ₹10 coin two ₹2 coin and one ₹1 coin. Proceed similarly for the second case.
"""

def count_ways_to_sum(N: int, coins: tuple) -> int:
    """
    Counts the number of ways to sum up to N using the given coins.

    Parameters:
    - N (int): The sum to be achieved.
    - coins (tuple): A tuple containing four integers representing the number of ₹1, ₹2, ₹5, and ₹10 coins respectively.

    Returns:
    - int: The number of ways to achieve the sum N using the given coins.
    """
    cs0 = coins
    r = 0
    for i in range(min(cs0[3], N // 10) + 1):
        for j in range(min(cs0[2], (N - i * 10) // 5) + 1):
            cs = list(cs0)
            N1 = N - 10 * i - 5 * j
            if 2 * cs[1] + cs[0] < N1 or (N1 % 2 == 1 and cs[0] == 0):
                continue
            if N1 % 2 == 1:
                N1 -= 1
                cs[0] -= 1
            if cs[0] % 2 == 1:
                cs[0] -= 1
            min2 = max(N1 - cs[0], 0) // 2
            max2 = min(N1 // 2, cs[1])
            r += max2 - min2 + 1
    return r