"""
QUESTION:
Chef has decided to start a new software company, the company's building has N offices numbered from 0 to N-1 and there's a computer in each office.

All offices' computers should be connected within a single network, so it's required to buy some ethernet cables and hubs. a cable connecting i-th office with j-th office has cost C_{i,j} also if the i-th office is connected with j other offices then it's required to buy a hub with capacity j and this will cost H_{i,j}, note that even if the hub with higher capacity is cheaper than the hub with capacity j the company will still buy the hub with capacity j. Each office should have exactly one hub.

Find a way for building the network so that all offices are connected to each other directly or indirectly while minimizing the total cost, it's not allowed to connect same pair of offices with more than one cable and it's not allowed to connect an office with itself.

Your solution is not required to find the most optimal solution. However, the less cost your solution will provide the more points you will get.

------ Input ------ 

Since the input is large you will not be given it directly. Instead, you will be given some parameters and the generator used to generate the input.

The first line contains a single integer T denoting the number of test-cases

The first line of each test-case contains the integers N, C_{max}, H_{max}

The following 2*N lines, each contain two integers Seed_{i,1}, Seed_{i,2} the seeds required for generating the input.

Using one of the generators, C++ generator, java generator, python 2 generator you will get C and H arrays.

------ Output ------ 

For each test-case output N lines, each line contains a string of N characters. if you want to connect i-th office and j-th office with a cable then i-th character of j-th line and  j-th character of i-th line both should be '1' otherwise they should be '0'. Note that i-th character of i-th line should always be '0' because you can't connect an office with itself.

Note that cables information is enough to uniquely determine what hub should be bought for each office.

------ Constraints ------ 

$T = 5$
$N = 1000$
$0 ≤ C_{i,j} ≤ 1,000,000$
$0 ≤ H_{i,j} ≤ 1,000,000$
$ C_{i,j} = C_{j,i}$
$ C_{i,i} = 0$
$0 < Seed_{i,1}, Seed_{i,2} < 10^{18}$

------ Test Generation ------ 

There will be 10 test-files.

The cost of a cable is chosen uniformly at random between 0 and C_{max} and the cost of a hub is chosen uniformly at random between 0 and H_{max}.

In each of the 10 test-files there are 5 test-cases, the values of C_{max} and H_{max} are:

$First test-case: C_{max} = 40,000 and H_{max} = 1,000,000$
$Second test-case: C_{max} = 100,000 and H_{max} = 1,000,000$
$Third test-case: C_{max} = 200,000 and H_{max} = 1,000,000$
$Fourth test-case: C_{max} = 500,000 and H_{max} = 1,000,000$
$Fifth test-case: C_{max} = 1,000,000 and H_{max} = 1,000,000$

All seeds in input are randomly generated.

------ Scoring ------ 

You will receive a WA if you didn't follow output format or there is a pair of offices which are not connected.

Your score in a single test-case is equal to the cost of the network outputed in that test-case, your overall score is the sum of scores of all test-cases in all test-files.

During contest you will be able to get your score on first 2 test-files. After contest there will be rejudge on full tests set.

------ Example ------ 

Input:
1
4 10 20
123456789012 4567890123456
11111111111111 2222222222222
101010101010 2323232323232
112358132134 1928374655647
999999555555 5555559999999
234123124155 1241352352345
234213515123 1231245551223
523432523332 1234124515123

Output:
0111
1000
1000
1000

------ Explanation ------ 

Example case 1. note that the example doesn't follow constraints on T and N and also seeds are set by hand in this sample.

In this example we have the array C:

0 0 7 6
0 0 2 7
7 2 0 7
6 7 7 0

and the array H

9 10 2 0
7 9 0 7
9 3 15 18
10 3 20 5

In the output, first office is connected all other offices and that will make the cost of the network equal to S = 0 + 7 + 6 + 0 + 9 + 3 + 3 = 28, so the score on this test-case is 28.
"""

import math

def xorshift128plus(s):
    (x, y) = s
    x ^= x << 23 & 2 ** 64 - 1
    s[0] = y
    s[1] = x ^ y ^ x >> 17 ^ y >> 26
    return y

def generate_cost_matrix(n, max_value, seeds):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        s = seeds[i]
        for j in range(i + 1, n):
            matrix[i][j] = matrix[j][i] = xorshift128plus(s) % (max_value + 1)
    return matrix

def minimize_network_cost(T, test_cases):
    results = []
    for t in range(T):
        (N, Cmax, Hmax, seeds_C, seeds_H) = test_cases[t]
        
        # Generate C and H matrices
        C = generate_cost_matrix(N, Cmax, seeds_C)
        H = generate_cost_matrix(N, Hmax, seeds_H)
        
        # Initialize the network matrix
        N_matrix = [[0] * N for _ in range(N)]
        
        # Connect each office to the first office
        for i in range(1, N):
            N_matrix[0][i] = 1
            N_matrix[i][0] = 1
        
        # Convert the network matrix to the required output format
        result = []
        for i in range(N):
            result.append(''.join(map(str, N_matrix[i])))
        
        results.append(result)
    
    return results