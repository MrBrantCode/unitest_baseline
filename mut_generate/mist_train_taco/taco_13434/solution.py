"""
QUESTION:
Given a set of N jobs where each job_{i} has a deadline and profit associated with it. 
Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline. 
Find the number of jobs done and the maximum profit.
Note: Jobs will be given in the form (Job_{id}, Deadline, Profit) associated with that Job.
Example 1:
Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job_{1} and Job_{3 }can be done with
maximum profit of 60 (20+40).
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
You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit as a list or vector of 2 elements.
Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)
Constraints:
1 <= N <= 10^{5}
1 <= Deadline <= N
1 <= Profit <= 500
"""

def job_scheduling(N, Jobs):
    # Find the maximum deadline to determine the size of the dp array
    max_d = max(job[1] for job in Jobs)
    
    # Sort jobs by profit in descending order
    Jobs.sort(key=lambda x: -x[2])
    
    # Initialize the dp array with zeros
    dp = [0] * max_d
    
    # Iterate over each job
    for job in Jobs:
        # Find the latest possible slot for the current job
        for j in range(min(max_d - 1, job[1] - 1), -1, -1):
            if dp[j] == 0:
                dp[j] = job[2]
                break
    
    # Calculate the number of jobs done and the maximum profit
    jobs_done = 0
    max_p = 0
    for p in dp:
        if p > 0:
            jobs_done += 1
            max_p += p
    
    return (jobs_done, max_p)