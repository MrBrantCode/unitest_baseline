"""
QUESTION:
Given an array of job difficulties, an array of corresponding profits, and an array of worker capabilities, write a function `maxProfitAssignment(difficulty, profit, worker)` that returns the maximum possible total profit that can be earned by assigning jobs to workers. Each worker can only undertake a job with a difficulty level not exceeding their capability, and a single job can be executed multiple times. If a worker is unable to complete any job, their earnings will be $0. Note that `1 <= difficulty.length = profit.length <= 10000`, `1 <= worker.length <= 10000`, and `difficulty[i], profit[i], worker[i]` are within the range `[1, 10^5]`.
"""

def bestJobAssignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    worker.sort()
    i = j = best = total = 0
    for w in worker:
        while j < len(jobs) and w >= jobs[j][0]:
            best = max(best, jobs[j][1])
            j += 1
        total += best
    return total