"""
QUESTION:
Sevenkplus was interested in contributing a challenge to hackerrank and he came up with this problem. 

You are given a linear congruence system with n variables and m equations: 

a_{11} x_{1} + a_{12} x_{2} + ... + a_{1n} x_{n} = b_{1} (mod p) 

a_{21} x_{1} + a_{22} x_{2} + ... + a_{2n} x_{n} = b_{2} (mod p) 

... 

a_{m1} x_{1} + a_{m2} x_{2} + ... + a_{mn} x_{n} = b_{m} (mod p)   

where, 

p is a prime number 

0 <= a_{ij} < p 

0 <= x_{i} < p 

0 <= b_{i} < p  

Given integers n, m, p, a, b, count the number of solutions to this equation. Since the output can be large, please output your answer modulo 10^9+7.

He writes the standard solution and a test data generator without difficulty, and generates some test data. 
However, when he attempts to remove hidden folders from the problem folder before uploading, he accidentally deletes the input file. 
Luckily, the output file remains and he still remembers some features of the input. He remembers n, m, p and that w entries of a are zero. However, he cannot recall more about the input. 

He wants to count how many possible inputs are there that will result in the desired output S (number of solutions to the equation system) output modulo 10^9+7. Can you help Sevenkplus?

Input Format 

The first line contains an integer T. T testcases follow. 
For each test case, the first line contains five numbers, m, n, p, S, w. separated by a single space. 

w lines follow. Each line contains two numbers x, y, which indicates that a_{xy}=0.

Output Format 

For each test case, output one line in the format Case #t: ans, where t is the case number (starting from 1), and ans is the answer. 

Constraints 

1 ≤ T ≤ 33 

1 <= m, n <= 1000 

p <= 10^9, p is a prime number 

0 <= S < 10^9+7 

w <= 17 

1 <= x <= m 

1 <= y <= n 

In any test case, one pair (x, y) will not occur more than once.

Sample Input

6
2 2 2 0 1
1 1
2 2 2 1 1
1 1
2 2 2 2 1
1 1
2 2 2 3 1
1 1
2 2 2 4 1
1 1
488 629 183156769 422223791 10
350 205
236 164
355 8
3 467
355 164
350 467
3 479
72 600
17 525
223 370

Sample Output

Case #1: 13
Case #2: 8
Case #3: 10
Case #4: 0
Case #5: 1
Case #6: 225166925

Explanation  

For test case 1, the 13 possible equations are:

a11 a12 b1  a21 a22 b2
0   0   0   0   0   1
0   0   1   0   0   0
0   0   1   0   0   1
0   0   1   0   1   0
0   0   1   0   1   1
0   0   1   1   0   0
0   0   1   1   0   1
0   0   1   1   1   0
0   0   1   1   1   1
0   1   0   0   0   1
0   1   0   0   1   1
0   1   1   0   0   1
0   1   1   0   1   0

Timelimits 

Timelimits for this challenge is given here
"""

def count_possible_inputs(T, test_cases):
    results = []
    for t in range(T):
        m, n, p, S, w, zero_positions = test_cases[t]
        # Placeholder for actual logic to compute the number of possible inputs
        # This logic needs to be implemented based on the problem statement
        ans = compute_possible_inputs(m, n, p, S, w, zero_positions)
        results.append(f"Case #{t+1}: {ans}")
    return results

def compute_possible_inputs(m, n, p, S, w, zero_positions):
    # This function should contain the logic to compute the number of possible inputs
    # that result in the desired number of solutions S.
    # For now, it returns a placeholder value.
    return 0  # Placeholder return value