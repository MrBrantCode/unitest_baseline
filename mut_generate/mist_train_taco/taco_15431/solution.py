"""
QUESTION:
Zonal Computing Olympiad 2015, 29 Nov 2014

An interval is a pair of positive integers [a, b] with a ≤ b. It is meant to denote the set of integers that lie between the values a and b. For example [3,5] denotes the set {3,4,5} while the interval [3, 3] denotes the set {3}.

We say that an interval [a, b] is covered by an integer i, if i belongs to the set defined by [a, b]. For example interval [3, 5] is covered by 3 and so is the interval [3, 3].

Given a set of intervals I, and a set of integers S we say that I is covered by S if for each interval [a, b] in I there is an integer i in S such that [a, b] is covered by i. For example, the set {[3, 5], [3, 3]} is covered by the set {3}. The set of intervals {[6, 9], [3, 5], [4, 8]} is covered by the set {4, 5, 8}. It is also covered by the set {4, 7}.

We would like to compute, for any set of intervals I, the size of the smallest set S that covers it. You can check that for the set of intervals {[6, 9], [3, 5], [4, 8]} the answer is 2 while for the set of intervals {[3, 5], [3, 3]} the answer is 1.

Your program should take the set of intervals as input and output the size of the smallest set that covers it as the answer.

-----Input format-----
The first line contains a single integer N, giving the number of intervals in the input.

This is followed by N lines, each containing two integers separated by a space describing an interval, with the first integer guaranteed to be less than or equal to the second integer.

-----Output format-----
Output a single integer giving the size of the smallest set of integers that covers the given set of intervals.

-----Test data-----
You may assume that all integers in the input are in the range 1 to 10^8 inclusive.

Subtask 1 (100 marks) : 1 ≤ N ≤ 5000.

-----Sample Input 1-----
2 
3 5 
3 3

-----Sample Output 1-----
1

-----Sample Input 2-----
3 
6 9 
3 5 
4 8

-----Sample Output 2-----
2
"""

def find_smallest_covering_set_size(intervals):
    # Sort intervals based on the starting point
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the current interval to the first interval
    curr = intervals[0]
    answer = 1
    
    # Iterate through the intervals starting from the second one
    for i in range(1, len(intervals)):
        if curr[1] < intervals[i][0]:
            # If the current interval does not overlap with the next interval,
            # increment the answer and update the current interval
            answer += 1
            curr = intervals[i]
        else:
            # If the current interval overlaps with the next interval,
            # update the current interval to cover the overlapping region
            curr[0] = intervals[i][0]
            curr[1] = min(curr[1], intervals[i][1])
    
    return answer