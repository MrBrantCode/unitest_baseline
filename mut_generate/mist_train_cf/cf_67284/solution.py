"""
QUESTION:
Write a function called `quicksort_space_complexity` that explains the space complexity of the Divide-and-Conquer strategy embedded Quicksort algorithm, utilizing the standard big O notation terminology. Assume the version of Quicksort that uses in-place partition algorithm which doesn’t need auxiliary array in the splitting process. The function should return the worst-case and best-case or average-case space complexity of the Quicksort algorithm in terms of the input size n.
"""

def quicksort_space_complexity(n):
    """
    This function returns the space complexity of the Quicksort algorithm.
    
    The Quicksort algorithm is a divide-and-conquer strategy embedded sorting algorithm 
    frequently used for its efficiency. It operates by selecting a 'pivot' element from 
    the array and partitioning the other elements into two sub-arrays, according to 
    whether they are less than or greater than the pivot. This process is then repeated 
    for the sub-arrays.
    
    The space complexity of the Quicksort algorithm in the worst-case scenario is O(n). 
    This case arises when the partition process always picks greatest or smallest element 
    as pivot, leading to skewed partitioning where one partition has n-1 elements and 
    the other has 0.
    
    However, in the best-case or average scenario, the Quicksort algorithm has a space 
    complexity of O(log n). This is due to the fact that in an ideal situation where 
    the pivot always divides the array/sub-array into two nearly equal halves, the 
    depth of the recursive tree becomes logarithmic to the input size (n). Since only 
    the auxiliary space required by the call stack is considered in the space complexity, 
    it would lead us to O(log n), with each level requiring constant auxiliary space.
    
    Parameters:
    n (int): The input size
    
    Returns:
    str: The worst-case and best-case or average-case space complexity of the Quicksort algorithm
    """
    
    worst_case = "O(n)"
    best_case = "O(log n)"
    
    return f"The space complexity of the Quicksort algorithm is {worst_case} in the worst-case scenario and {best_case} in the best-case or average-case scenario."