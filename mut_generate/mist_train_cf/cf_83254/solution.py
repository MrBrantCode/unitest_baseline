"""
QUESTION:
Given an array of projects where each project is represented as [startDay, endDay, profit] and an integer n representing the maximum number of projects that can be completed, write a function jobScheduling(projects, n) to find the maximum sum of profits that can be received by completing projects. Each project can only be worked on one at a time and must be completed in its entirety. The end day of a project is inclusive, meaning a new project cannot start on the same day another one ends. Return the maximum sum of profits.
"""

from typing import List
import bisect

def jobScheduling(projects: List[List[int]], n: int) -> int:
    """
    This function finds the maximum sum of profits that can be received by completing projects.
    
    Args:
        projects (List[List[int]]): A list of projects where each project is represented as [startDay, endDay, profit].
        n (int): The maximum number of projects that can be completed.
        
    Returns:
        int: The maximum sum of profits.
    """
    jobs = sorted(zip([i[0] for i in projects], [i[1] for i in projects], [i[2] for i in projects]), key=lambda v: v[1])
    dp = [[0, 0]]
    
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
            
    return dp[-1][1]