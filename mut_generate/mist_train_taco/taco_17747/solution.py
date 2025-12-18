"""
QUESTION:
problem

There is one bar-shaped candy with a length of N mm (where N is an even number). Two JOI officials decided to cut this candy into multiple pieces and divide them into a total of N / 2 mm. did.

For unknown reasons, this candy has different ease of cutting depending on the location. The two examined the candy every millimeter from the left and figured out how many seconds it would take to cut at each location. .2 Create a program that finds the minimum number of seconds it takes for a person to cut a candy.

output

The output consists of one line containing the minimum number of seconds it takes for two people to cut the candy.

Input / output example

Input example 1


6
1
8
12
6
2


Output example 1


7


In this case, cutting 1 and 4 millimeters from the left edge minimizes the number of seconds. The number of seconds is 1 and 6 seconds, for a total of 7 seconds.

<image>

The above question sentences and the data used for the automatic referee are the question sentences created and published by the Japan Committee for Information Olympics and the test data for scoring.



input

The length of the bar N (2 ≤ N ≤ 10000, where N is an even number) is written on the first line of the input. On the first line of the input i + (1 ≤ i ≤ N − 1), An integer ti (1 ≤ ti ≤ 10000) is written to represent the number of seconds it takes to cut the i-millimeter location from the left edge. Note that there are N − 1 locations that can be cut.

Of the scoring data, the minimum value can be achieved by cutting at most 2 points for 5% of the points, and the minimum value can be achieved by cutting at most 3 points for 10%. For 20% of the points, N ≤ 20.

Example

Input

6
1
8
12
6
2


Output

7
"""

def minimum_cut_time(N, cost):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N):
        for j in range(i):
            if dp[i - j] + cost[i - 1] < dp[j]:
                dp[j] = dp[i - j] + cost[i - 1]
            if dp[j] + cost[i - 1] < dp[i - j]:
                dp[i - j] = dp[j] + cost[i - 1]
    
    return dp[N // 2]