"""
QUESTION:
Once N boys and M girls attended a party. You are given a matrix A of N rows and M columns where Aij is 1 if the i-th boy likes the j-th girl, otherwise it will be 0. Note that it is not necessary that if a boy x likes girl y, then girl y should like boy x.
You know that if there are two different boys x and y, who both like girl z, then there will be a collision.
Can you calculate the number of different collisions at this party? Note that order of boys in the collision doesn't matter.

-----Input-----
The first line contains a single integer T denoting the number of test cases. Then T test cases follow.
The first line of each test case contains two space separated integers N, M denoting the number of boys and girls, respectively.
Each of the following N lines contain M characters, each of them is either '0' or '1'.

-----Output-----
For each test case output a single line containing an integer corresponding to the number of collisions at the party.

-----Constraints-----
- 1 ≤ T ≤ 100
- 1 ≤ N, M ≤ 10

-----Example-----
Input:
2
4 3
111
100
110
000
2 2
10
01

Output:
4
0

-----Explanation-----
Example Case 1. All three boys like the first girl, so there are (1, 2, 1), (1, 3, 1), (2, 3, 1) collisions with her. Boys 1 and 3 both like the second girl so this is one more collision. Only one boy likes the third girl, so there are no collisions with her and thus we have 4 collisions total.
Example Case 2. For each girl there is only one boy who likes her, so there are no collisions at all.
"""

def calculate_collisions(test_cases):
    results = []
    
    for case in test_cases:
        n, m, matrix = case
        temp_list = [0] * m
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    temp_list[j] += 1
        
        ans = 0
        for k in temp_list:
            if k > 1:
                ans += (k - 1) * k // 2
        
        results.append(ans)
    
    return results