"""
QUESTION:
The function `minimumTimeRequired` takes an integer array `jobs` and an integer `k` as inputs. The function returns the least possible maximum working duration of any allocation of tasks to `k` employees, where each task must be allocated to precisely one employee. The function must satisfy the constraints that `1 <= k <= jobs.length <= 12` and `1 <= jobs[i] <= 10^7`.
"""

def minimumTimeRequired(jobs, k):
    def check(limit):
        def dfs(idx, workload):
            if idx == len(jobs):
                return True
            cur = jobs[idx]
            for i in range(len(workload)):
                if workload[i] + cur <= limit:
                    workload[i] += cur
                    if dfs(idx + 1, workload):
                        return True
                    workload[i] -= cur
                if workload[i] == 0:
                    break
            return False

        return dfs(0, [0] * k)

    jobs.sort(reverse=True)
    l, r = jobs[0], sum(jobs)
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l