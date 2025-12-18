"""
QUESTION:
When Misha hits his favorite gym, he comes across an interesting problem with the barbell. In the gym, someone always leaves the weight plates in the strangest places you can imagine and sometime it's difficult to equip the barbell the way you want. Let's imagine that you have N weight plates placed in any order (remember that any gym has no more than K different types of weight plates and all weights are square-free). As a preliminary step towards solving this problem, Misha wants to simulate a simple gym, and for this purpose you have to deal with some queries:

- [1 I X] Set the weight of the ith weight plate to value X.

- [2 L R] Reverse the sequence of weight plates in the interval from L to R, where 1 ≤ L ≤ R ≤ N.

- [3 L R W] Check the interval from L to R to find out if you can make the weight W using only weight plates on this interval. (Note: this type of query will appear no more than P times)

Please help Misha in solving this problem. 

-----Input-----
First line of input contains the number of weight plates N, and number of queries Q. Next line contains N integers w1, w2, ..., wN, where wi is the weight of the ith weight plate. Next Q lines contain some queries described above. 

-----Output-----
For all queries of the third type: print "Yes" if your check returns a positive outcome, and "No" otherwise.

-----Constraints-----
- 1 ≤ N, W, Q ≤ 105
- K ≤ 10
- P ≤ 1000
- All numbers in the input are positive integers and ≤ 105.
- All the weights are square-free.

-----Subtasks-----
- Subtask 1: 1 ≤ N ≤ 103, 1 ≤ W ≤ 103, Q = 1 - 10 pts.

- Subtask 2: 1 ≤ N ≤ 103, 1 ≤ W ≤ 103, 1 ≤ Q ≤ 103, P ≤ 100 - 15 pts
- Subtask 3: 1 ≤ N ≤ 104, 1 ≤ W ≤ 104, 1 ≤ Q ≤ 104, P ≤ 300 - 25 pts.

- Subtask 4: 1 ≤ N ≤ 105, 1 ≤ W ≤ 105, 1 ≤ Q ≤ 105, K ≤ 2 - 20 pts.

- Subtask 5: Original constraints - 30 pts.

-----Example-----First
Input:5 10
1 2 3 5 6
3 2 3 3
3 2 3 4
3 2 3 5
2 2 5
3 2 4 8
1 2 1
3 2 4 8
2 1 4 
3 2 4 3 
3 1 5 7 

Output:Yes
No
Yes
Yes
Yes
No
YesSecond
Input:3 4
2013 2015 2017
3 1 3 4030
1 1 111
3 1 3 4030
3 1 2 111

Output:Yes
No
Yes

-----Explanation:-----First test explanation (step by step)
1 2 3 5 6
3 2 3 3 ([2, 3] 3=3 => Yes)
3 2 3 4 ([2, 3] can't make 4 => No)
3 2 3 5 ([2, 3] 2+3=5 => Yes)
2 2 5 (Reverse: [1, 6, 5, 3, 2])
3 2 4 8 ([6, 5, 3] 5+3=8 => Yes)
1 2 1 (Set: [1, 1, 5, 3, 2])
3 2 4 8 ([1, 5, 3] 5+3=8 => Yes)
2 1 4  (Reverse: [3, 5, 1, 1, 2])
3 2 4 3 ([5, 1, 1] can't make 3 => No)
3 1 5 7 ([3, 5, 1, 1, 2] 2+1+1+3=7 => Yes)
"""

def process_queries(N, Q, weights, queries):
    results = []
    
    def fx(s, n, xsum):
        sub = [[None for _ in range(n + 2)] for _ in range(xsum + 2)]
        for i in range(n + 1):
            sub[0][i] = True
        for i in range(1, xsum + 1):
            sub[i][0] = False
        for i in range(1, xsum + 1):
            for j in range(1, n + 1):
                sub[i][j] = sub[i][j - 1]
                if i >= s[j - 1]:
                    sub[i][j] = sub[i][j] or sub[i - s[j - 1]][j - 1]
        return sub[xsum][n]
    
    for query in queries:
        if query[0] == 1:
            # Set the weight of the ith weight plate to value X
            weights[query[1] - 1] = query[2]
        elif query[0] == 2:
            # Reverse the sequence of weight plates in the interval from L to R
            L, R = query[1] - 1, query[2]
            weights[L:R] = weights[L:R][::-1]
        elif query[0] == 3:
            # Check the interval from L to R to find out if you can make the weight W
            L, R, W = query[1] - 1, query[2], query[3]
            interval_weights = weights[L:R]
            if W < min(interval_weights) or W > sum(interval_weights):
                results.append('No')
            elif W in interval_weights:
                results.append('Yes')
            else:
                if fx(interval_weights, len(interval_weights), W):
                    results.append('Yes')
                else:
                    results.append('No')
    
    return results