"""
QUESTION:
Given two arrays of the same length representing daily precipitation and water usage, write a function `calculate_container_size` that calculates the minimum size of a container required to save water during dry days (days with zero precipitation). The function should take two lists, `precipitations` and `water_usages`, as input and return the minimum container size required to compensate for the worst-case scenario of consecutive dry days.
"""

def calculate_container_size(precipitations, water_usages):
    diffs = [rain - usage for rain, usage in zip(precipitations, water_usages)]
    container_size = 0
    running_total = 0
    
    for diff in diffs:
        running_total += diff
        if running_total < container_size:
            container_size = running_total
        if running_total > 0:
            running_total = 0
            
    return -container_size