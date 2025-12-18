"""
QUESTION:
Petya is a math teacher. n of his students has written a test consisting of m questions. For each student, it is known which questions he has answered correctly and which he has not.

If the student answers the j-th question correctly, he gets p_j points (otherwise, he gets 0 points). Moreover, the points for the questions are distributed in such a way that the array p is a permutation of numbers from 1 to m.

For the i-th student, Petya knows that he expects to get x_i points for the test. Petya wonders how unexpected the results could be. Petya believes that the surprise value of the results for students is equal to ∑_{i=1}^{n} |x_i - r_i|, where r_i is the number of points that the i-th student has got for the test.

Your task is to help Petya find such a permutation p for which the surprise value of the results is maximum possible. If there are multiple answers, print any of them.

Input

The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers n and m (1 ≤ n ≤ 10; 1 ≤ m ≤ 10^4) — the number of students and the number of questions, respectively.

The second line contains n integers x_1, x_2, ..., x_n (0 ≤ x_i ≤ (m(m+1))/(2)), where x_i is the number of points that the i-th student expects to get.

This is followed by n lines, the i-th line contains the string s_i (|s_i| = m; s_{i, j} ∈ \{0, 1\}), where s_{i, j} is 1 if the i-th student has answered the j-th question correctly, and 0 otherwise.

The sum of m for all test cases does not exceed 10^4.

Output

For each test case, print m integers — a permutation p for which the surprise value of the results is maximum possible. If there are multiple answers, print any of them.

Example

Input


3
4 3
5 1 2 2
110
100
101
100
4 4
6 2 0 10
1001
0010
0110
0101
3 6
20 3 15
010110
000101
111111


Output


3 1 2 
2 3 4 1 
3 1 4 5 2 6
"""

def maximize_surprise_value(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, expected_points, correct_answers = case
        M = [list(map(int, list(answers))) for answers in correct_answers]
        o = [bin(i).count('1') for i in range(1 << n)]
        q = [sum((1 << i for i in range(n) if M[i][j])) for j in range(m)]
        b = -1
        
        for i in range(1 << n):
            c = [0] * (n + 1)
            v = [0] * m
            d = c[:]
            P = v[:]
            
            for j in range(m):
                v[j] = o[i ^ q[j]]
                c[v[j]] += 1
            
            for j in range(n):
                d[j + 1] = d[j] + c[j]
            
            for j in range(m):
                d[v[j]] += 1
                P[j] = d[v[j]]
            
            T = 2 * sum((expected_points[j] for j in range(n) if i >> j & 1)) - sum(expected_points) + sum(((o[q[j]] - 2 * o[i & q[j]]) * P[j] for j in range(m)))
            
            if T > b:
                b, p = T, P
        
        results.append(p)
    
    return results