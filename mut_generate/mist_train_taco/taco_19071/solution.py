"""
QUESTION:
Harry was contesting to be the most stylist person in his college. He had to collect maximum points from the judges to be able to win. However there was a problem. The judges were sitting in a line and each pair of adjacent judges had ego issues with each other. So if one judge gave X points to Harry then the next judge won’t give him any points. Harry had a friend in the organizing team and through him he had found out the exact points he would get from each judge if he chose their score to be considered. Help him find out the maximum points he can score.

INPUT
The first line of input contains the number of test cases, T.
0 < T < = 10
Each test case starts with a number N, the number of judges.
0 ≤ N < = 10^4. 
The next line will have N numbers, number of points each judge gave Harry
0 < = X(i) < = 10^9.
 The order of the judges does not change.

OUTPUT
For each test case print “Case T: A” without quotes in a single line. 
T is the case number, starting with 1.
A is the maximum number of points Harry can collect.

SAMPLE INPUT
2
5
1 2 3 4 5
1
10

SAMPLE OUTPUT
Case 1: 9
Case 2: 10

Explanation

Case 1 : 
Harry chooses judges 1,3 and 5 with points 1 ,3 and 5 respectively to add up to 9 points in total.
Case 2:
There is only one judge so Harry chooses his points alone.
"""

def calculate_max_points(test_cases):
    results = []
    
    for idx, case in enumerate(test_cases):
        N = case[0]
        points = case[1]
        
        if N == 0:
            results.append(f"Case {idx + 1}: 0")
            continue
        
        dp = [0] * N
        
        for i in range(N):
            if i == 0:
                dp[i] = points[i]
            elif i == 1:
                dp[i] = max(points[i], dp[i - 1])
            else:
                dp[i] = max(points[i] + dp[i - 2], dp[i - 1])
        
        results.append(f"Case {idx + 1}: {dp[-1]}")
    
    return results