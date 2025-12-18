"""
QUESTION:
Have you ever implemented a program adding two big integers that cannot be represented by the primitive data type of your programming language? The algorithm is just simulation of the column addition method that we have been taught in elementary school. Sometimes we forget the carry and the result is incorrect. 
In this problem, you need to evaluate the expected value of the number of times we have non-zero carry when adding two non-negative integers that contain at most N digits each. Note that we are adding the numbers in their base 10 representation.

For example, the following table shows the number of carries when adding some pairs of numbers: 

A
		B		
		Number of carries
	20
		4		
		0
	111
		119		
		1
	123
		923		
		1
	1235
		98765		
		5
	
------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. 
Each test case has a single line containing an integer N.

------ Output ------ 

For each test case, output a single line containing the required expected value. 
Your answer will be accepted if the error is less than 10 ^{-6}.

------ Constraints ------ 

$1 ≤ T ≤ 100,000(10^{5})$
$1 ≤ N ≤ 100,000(10^{5})$

----- Sample Input 1 ------ 
3
1
2
3
----- Sample Output 1 ------ 
0.45
0.945
1.4445
----- explanation 1 ------ 
Example case 1.
We have 10*10 = 100 cases of adding two 1-digit number.
The carry appears when adding 1 and 9, 2 and 9, 3 and 9 ... and so on, 
there are 45 cases in total and in each case, the carry appears exactly once.
"""

def expected_carries(T: int, N_list: list) -> list:
    """
    Calculate the expected value of the number of times we have non-zero carry 
    when adding two non-negative integers that contain at most N digits each.

    Parameters:
    T (int): Number of test cases.
    N_list (list): List of integers where each integer represents the maximum number of digits for each test case.

    Returns:
    list: List of expected values corresponding to each test case.
    """
    p = 10 ** 5 + 9
    dp = [0] * p
    pre = [0] * p
    
    dp.append(0)
    dp.append(0.45)
    
    for i in range(2, p):
        dp[i] = 0.45 + 10 * dp[i - 1] / 100
    
    for i in range(1, p):
        pre[i] = pre[i - 1] + dp[i]
    
    results = [pre[n + 1] for n in N_list]
    
    return results