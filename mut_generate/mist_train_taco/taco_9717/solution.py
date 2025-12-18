"""
QUESTION:
Zonal Computing Olympiad 2012, 26 Nov 2011

The year is 2102 and today is the day of ZCO. This year there are N contests and the starting and ending times of each contest is known to you. You have to participate in exactly one of these contests. Different contests may overlap. The duration of different contests might be different. 

There is only one examination centre. There is a wormhole V that transports you from your house to the examination centre and another wormhole W that transports you from the examination centre back to your house. Obviously, transportation through a wormhole does not take any time; it is instantaneous. But the wormholes can be used at only certain fixed times, and these are known to you.

So, you use a V wormhole to reach the exam centre, possibly wait for some time before the next contest begins, take part in the contest, possibly wait for some more time and then use a W wormhole to return back home. If you leave through a V wormhole at time t1 and come back through a W wormhole at time t2, then the total time you have spent is (t2 - t1 + 1). Your aim is to spend as little time as possible overall while ensuring
that you take part in one of the contests.

You can reach the centre exactly at the starting time of the contest, if possible. And you can leave the examination centre the very second the contest ends, if possible. You can assume that you will always be able to attend at least one contest–that is, there will always be a contest such that there is a V wormhole before it and a W wormhole after it.

For instance, suppose there are 3 contests with (start,end) times (15,21), (5,10), and (7,25), respectively.  Suppose the V wormhole is available at times 4, 14, 25, 2 and the W wormhole is available at times 13 and 21.  In this case, you can leave by the V wormhole at time 14, take part in the contest from time 15 to 21, and then use the W wormhole at time 21 to get back home.  Therefore the time you have spent is (21 - 14 + 1) = 8. You can check that you cannot do better than this.

-----Input format-----
The first line contains 3 space separated integers N, X, and Y, where N is the number of contests, X is the number of time instances when wormhole V can be used and Y is the number of time instances when wormhole W can be used.  The next N lines describe each contest.  Each of these N lines contains two space separated integers S and E, where S is the starting time of the particular contest and E is the ending time of that contest, with S < E.  The next line contains X space separated integers which are the time instances when the wormhole V can be used.  The next line contains Y space separated integers which are the time instances when the wormhole W can be used.

-----Output format-----
Print a single line that contains a single integer, the minimum time needed to be spent to take part in a contest.

-----Testdata-----
All the starting and ending times of contests are distinct and no contest starts at the same time as another contest ends. The time instances when wormholes are available are all distinct, but may coincide with starting and ending times of contests. All the time instances (the contest timings and the wormhole timings) will be integers between 1 and 1000000 (inclusive).

- Subtask 1 (30 marks)
- Subtask 2 (70 marks)

You may assume that 
1 ≤ N ≤ 105,
1 ≤ X ≤ 105, and
1 ≤ Y ≤ 105.

In 30% of the cases, 
1 ≤ N ≤ 103,
1 ≤ X ≤ 103, and
1 ≤ Y ≤ 103.

-----Sample Input-----
3 4 2
15 21
5 10
7 25
4 14 25 2
13 21

-----Sample Output-----
8
"""

def calculate_minimum_time(N, X, Y, contests, v_times, w_times):
    import sys
    
    # Sort the lists of wormhole times
    v_times.sort()
    w_times.sort()
    
    # Initialize the minimum time to a large value
    min_time = sys.maxsize
    
    # Iterate over each contest
    for (start, end) in contests:
        # Find the latest V wormhole time before the contest starts
        v_index = -1
        for i in range(X):
            if v_times[i] > start:
                break
            v_index = i
        
        # Find the earliest W wormhole time after the contest ends
        w_index = -1
        for j in range(Y):
            if w_times[j] >= end:
                w_index = j
                break
        
        # If valid V and W wormhole times are found, calculate the time spent
        if v_index != -1 and w_index != -1:
            v_time = v_times[v_index]
            w_time = w_times[w_index]
            time_spent = w_time - v_time + 1
            min_time = min(min_time, time_spent)
    
    return min_time