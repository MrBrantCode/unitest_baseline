"""
QUESTION:
Given a set of N jobs where each job_{i} has a deadline and profit associated with it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the number of jobs done and the maximum profit.
Note: Jobs will be given in the form (Job_{id}, Deadline, Profit) associated with that Job.
Example 1:
Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Since at deadline 1 Job3 can give the maximum profit and for deadline 4 we left with only Job1 hence Job_{1} and Job_{3 }can be done with maximum profit of 60 (20+40).
Example 2:
Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).
Your Task :
You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns an array ans[ ] in which ans[0] contains the count of jobs and ans[1] contains maximum profit.
Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)
Constraints:
1 <= N <= 10^{5}
1 <= Deadline <= N
1 <= Profit <= 500
"""

def job_scheduling(N, Jobs):
    # Initialize a list to keep track of the maximum profit for each deadline slot
    temp = [0] * N
    
    # Sort jobs by profit in descending order
    Jobs.sort(key=lambda job: job[2], reverse=True)
    
    # Iterate over each job
    for job in Jobs:
        deadline = job[1]
        profit = job[2]
        
        # Try to place the job in the latest possible slot before its deadline
        for j in range(deadline - 1, -1, -1):
            if temp[j] == 0:
                temp[j] = profit
                break
    
    # Calculate the number of jobs scheduled and the total profit
    count = 0
    total_profit = 0
    for profit in temp:
        if profit != 0:
            count += 1
            total_profit += profit
    
    return [count, total_profit]