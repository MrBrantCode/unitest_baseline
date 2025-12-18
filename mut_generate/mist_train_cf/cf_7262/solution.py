"""
QUESTION:
Implement a function `find_stats(vector)` that calculates the sum, product, average, maximum, minimum, and median of all elements in the given vector. The function should have a time complexity of O(n log n) due to the need to sort the vector to find the median, and a space complexity of O(log n) for the recursive call stack. The input vector will contain 10^6 random integers between -10^9 and 10^9.
"""

def find_stats(vector):
    n = len(vector)
    
    # Initialize minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    
    # Initialize sum and product
    total_sum = 0
    total_product = 1
    
    # Find minimum, maximum, sum, and product using divide-and-conquer
    def helper(start, end):
        nonlocal min_val, max_val, total_sum, total_product
        
        if start == end:
            num = vector[start]
            min_val = min(min_val, num)
            max_val = max(max_val, num)
            total_sum += num
            total_product *= num
            return
        
        mid = (start + end) // 2
        helper(start, mid)
        helper(mid + 1, end)
    
    helper(0, n - 1)
    
    # Find average
    average = total_sum / n
    
    # Find median
    vector.sort()
    median = vector[n // 2]
    
    return min_val, max_val, total_sum, total_product, average, median