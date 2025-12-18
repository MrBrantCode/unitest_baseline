"""
QUESTION:
Write a function `get_epidemic(result)` that takes a list `result` of integers representing the number of infected individuals for each day and returns a tuple containing the peak day of the epidemic (1-indexed) and the total number of days the epidemic lasted. The epidemic is considered to have ended when the number of infected individuals starts decreasing.
"""

def get_epidemic(result):
    peak_day = result.index(max(result)) + 1
    epidemic_duration = len(result)

    for i in range(peak_day, len(result)):
        if result[i] < result[i - 1]:  
            epidemic_duration = i  

    return peak_day, epidemic_duration