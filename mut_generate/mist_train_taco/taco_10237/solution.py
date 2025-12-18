"""
QUESTION:
Binod and his family live in Codingland. They have a festival called N-Halloween.
The festival is celebrated for N  consecutive days. On each day Binod gets some candies from his mother. He may or may not take them. On a given day ,  Binod will be sad if he collected candies on that day and he does not have at least X   candies remaining  from the candies he collected that day at the end of that day . His friend Pelu who is very fond of candies asks for X  candies from Binod on a day if Binod collects any candy on that day. He does so immediately after Binod collects them. Binod being a good friend never denies him.  

Given a list a   where ai   denotes the number of candies Binod may take on the ith   day and  Q  queries having a number X , find the maximum number of candies Binod can collect so that he won't be sad after the festival ends.
Input format: 

First-line contains two integers N and Q denoting the number of festival days and number of queries respectively.

The second line is the array whose ith   element is the maximum number of candies Binod may
collect on that day.

Each of the next Q lines contains the number X i.e the minimum number of candies Binod wants to have at the end of every day on which he collects any candy.
Output format: 

For every query output, a single integer denoting the max number of candies Binod may
collect (for the given X ) to be happy after the festival ends.
Constraints:  

1<=N,Q<=105  

1<=Q<=105  

0<=ai<=109  

0<=X<=109  

Sample Input : 

5 2

4 6 5 8 7

1

2

Sample Output : 

30

30

Sample Input:  

6 3 

20 10 12 3 30 5 

2 

6 

13 

Sample Output  

77 

62 

30 

Explanation: 

In the first query of sample input 1, Binod can collect the maximum number of given chocolates for a given day each day as after the end of every day Binod will have a number of collected
chocolates on that day greater than equal to 1 even after giving 1 chocolate to Pelu. So the
the answer is 4+6+5+8+7=30.
"""

import bisect

def max_candies_for_happiness(N, Q, candies_per_day, queries):
    # Sort the candies_per_day list
    candies_per_day.sort()
    
    # Create a prefix sum array to store cumulative sums
    prefix_sum = [0] * N
    prefix_sum[0] = candies_per_day[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + candies_per_day[i]
    
    results = []
    for x in queries:
        # Find the index where candies_per_day[i] >= 2 * x
        index = bisect.bisect_left(candies_per_day, 2 * x)
        
        # Calculate the maximum number of candies Binod can collect
        if index == 0:
            max_candies = prefix_sum[N - 1]
        else:
            max_candies = prefix_sum[N - 1] - prefix_sum[index - 1]
        
        results.append(max_candies)
    
    return results