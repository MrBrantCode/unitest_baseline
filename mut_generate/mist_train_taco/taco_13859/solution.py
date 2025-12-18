"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 
Chef likes problems related to numbers a lot. He is generally quite good at solving these kinds of problems, but today he got stuck at one number theory problem, and so he asks your help to solve it.

Given a positive integer N, find out how many positive integers X satisfy the equation X + S(X) + S(S(X)) = N, where S(X) denoting sum of digits of X in decimal (base 10) representation.

------ Input ------ 

The only line of the input contains one integer number - N.

------ Output ------ 

Output single integer in a line denoting the count of number of positive integers X satisfying the above given equation.

------ Constraints ------ 

$1 ≤ N ≤ 10^{9}$

----- Sample Input 1 ------ 
6
----- Sample Output 1 ------ 
1
----- explanation 1 ------ 
Example 1. Only one positive integer X = 2 satisfies the equation X + S(X) + S(S(X)) = 6, as X + S(X) + S(S(X)) = 2 + 2 + 2 = 6.

----- Sample Input 2 ------ 
9939
----- Sample Output 2 ------ 
4
----- explanation 2 ------ 
Example 2.X can be 9898, 9907, 9910 and 9913. 
9898 + S(9898) + S(S(9898)) = 9898 + 34 + 7 = 9939
9907 + S(9907) + S(S(9907)) = 9907 + 25 + 7 = 9939
9910 + S(9910) + S(S(9910)) = 9910 + 19 + 10 = 9939
9913 + S(9913) + S(S(9913)) = 9913 + 22 + 4 = 9939
You can verify that there is not other positive value of X satisfying the given equation.
"""

def sum_of_digits(num):
    """Helper function to calculate the sum of digits of a number."""
    si = 0
    while num:
        si += num % 10
        num = num // 10
    return si

def count_valid_X(N):
    """
    Function to count the number of positive integers X that satisfy the equation
    X + S(X) + S(S(X)) = N, where S(X) is the sum of digits of X.
    
    Parameters:
    - N (int): The given positive integer.
    
    Returns:
    - int: The count of valid X.
    """
    cnt = 0
    if N < 100:
        ra = 0
    else:
        ra = N - 100
    
    for i in range(ra, N):
        fi = sum_of_digits(i)
        se = sum_of_digits(fi)
        s = i + fi + se
        if s == N:
            cnt += 1
        elif s > N:
            break
    
    return cnt