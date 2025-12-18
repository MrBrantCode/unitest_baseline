"""
QUESTION:
The kingdom of Lazyland is the home to $n$ idlers. These idlers are incredibly lazy and create many problems to their ruler, the mighty King of Lazyland. 

Today $k$ important jobs for the kingdom ($k \le n$) should be performed. Every job should be done by one person and every person can do at most one job. The King allowed every idler to choose one job they wanted to do and the $i$-th idler has chosen the job $a_i$. 

Unfortunately, some jobs may not be chosen by anyone, so the King has to persuade some idlers to choose another job. The King knows that it takes $b_i$ minutes to persuade the $i$-th idler. He asked his minister of labour to calculate the minimum total time he needs to spend persuading the idlers to get all the jobs done. Can you help him? 


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le k \le n \le 10^5$) — the number of idlers and the number of jobs.

The second line of the input contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le k$) — the jobs chosen by each idler.

The third line of the input contains $n$ integers $b_1, b_2, \ldots, b_n$ ($1 \le b_i \le 10^9$) — the time the King needs to spend to persuade the $i$-th idler.


-----Output-----

The only line of the output should contain one number — the minimum total time the King needs to spend persuading the idlers to get all the jobs done.


-----Examples-----
Input
8 7
1 1 3 1 5 3 7 1
5 7 4 8 1 3 5 2

Output
10

Input
3 3
3 1 2
5 3 4

Output
0



-----Note-----

In the first example the optimal plan is to persuade idlers 1, 6, and 8 to do jobs 2, 4, and 6.

In the second example each job was chosen by some idler, so there is no need to persuade anyone.
"""

def calculate_minimum_persuasion_time(n, k, jobs, persuasion_times):
    # Calculate the number of jobs that need to be reassigned
    exch = k - len(set(jobs))
    
    # Initialize a list to track the minimum persuasion time for each job
    double_jobs = [0] * (k + 1)
    
    # List to store the persuasion times of idlers who chose the same job
    time_of_double = []
    
    # Iterate over each idler's job choice
    for i in range(n):
        job = jobs[i]
        time = persuasion_times[i]
        
        # If the current idler's persuasion time is less than the stored time for this job
        if double_jobs[job] < time:
            # If there was already an idler assigned to this job, add their time to the list
            if double_jobs[job] != 0:
                time_of_double.append(double_jobs[job])
            # Update the minimum persuasion time for this job
            double_jobs[job] = time
        else:
            # If the current idler's persuasion time is more, add it to the list
            time_of_double.append(time)
    
    # Sort the list of persuasion times for reassignment
    time_of_double.sort()
    
    # Calculate the minimum total time needed to persuade idlers
    minimum_time = sum(time_of_double[:exch])
    
    return minimum_time