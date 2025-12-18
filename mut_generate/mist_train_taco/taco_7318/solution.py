"""
QUESTION:
Read problems statements in Mandarin Chinese and Russian as well. 
You are given a function f which is defined as :
 
Your task is to find the value of 
 
where M is given in input.

------ Input Format ------ 

First line contains T, the number of test cases.

First line of each test case contain 3 space separated integers N, M and Q.

Next Q line follows, each line contain r.

------ Output Format ------ 

For each test case, output Q lines, each line containing the required answer.

------ Constraints ------ 

2 ≤ N ≤ 10^{6}

1 ≤ M ≤ 10^{9}

2 ≤ Sum of N over all test cases ≤ 10^{6}

1 ≤ Sum of Q over all test cases ≤ 2*10^{5}

1 ≤ T ≤ 10^{5}

1 < r < N

Sample Input
2
5 114 1
2
50 3874 3
31
17
21

Sample Output
72
3718
624
1144

Explanation for first test case 
f[1] = 1

f[2] = 2

f[3] = 1*2^{2} * 3 = 12

f[4] =1*2^{3}*3^{2}*4 = 8*9*4 = 288

f[5] = 1*2^{4}*3^{3}*4^{2}*5 =34560

value of f[5] / (f[2]*f[3]) = 1440 and 1440 %114 is 72
"""

def calculate_f_values(test_cases):
    results = []
    
    for case in test_cases:
        N, M, Q, queries = case
        ls = [0] * N
        ls[1] = N
        
        for i in range(2, N):
            ls[1] = ls[1] * i % M
        
        N += 1
        if N % 2:
            num, den, cur = N // 2 + 1, N // 2, N // 2 + 1
        else:
            num, den, cur = N // 2, N // 2, 1
        
        N -= 1
        ls[den] = cur
        num += 1
        den -= 1
        
        while den > 1:
            cur = cur * (den + 1) % M
            cur = cur * num % M
            ls[den] = cur
            num += 1
            den -= 1
        
        for i in range(2, N // 2 + 1):
            ls[i] = ls[i] * ls[i - 1] % M
        
        case_results = []
        for x in queries:
            if x > N / 2:
                x = N - x
            case_results.append(ls[x])
        
        results.append(case_results)
    
    return results