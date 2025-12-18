"""
QUESTION:
Write a recursive function `recursiveSum` that calculates the sum of all possible pairs of elements from two arrays `a` and `b`, where the length of `a` and `b` is not necessarily the same. The function should take five parameters: the current indices `i` and `j` for arrays `a` and `b` respectively, the arrays `a` and `b`, and a variable `sum` to store the result. 

The function should start the recursion from the beginning of both arrays and continue until all pairs are processed. 

Note that the operations of matrix multiplication, addition, and array referencing have a constant time complexity of O(1). Analyze the time and space complexity of the recursive algorithm.
"""

def recursiveSum(i, j, a, b, total_sum):
    """
    Recursively calculates the sum of all possible pairs of elements from two arrays.
    
    Args:
        i (int): The current index for array 'a'.
        j (int): The current index for array 'b'.
        a (list): The first array.
        b (list): The second array.
        total_sum (list): A list containing the running sum.
    
    Returns:
        None
    """
    # Base case: if we have processed all pairs, return
    if i == len(a) and j == len(b):
        return
    
    # If we haven't reached the end of array 'a', add the current pair and recurse
    if i < len(a):
        # Add the current pair to the sum
        total_sum[0] += a[i] + (b[j] if j < len(b) else 0)
        
        # Recurse with the next element in array 'a'
        recursiveSum(i + 1, j, a, b, total_sum)
    
    # If we haven't reached the end of array 'b', add the current pair and recurse
    if j < len(b):
        # Add the current pair to the sum
        total_sum[0] += (a[i] if i < len(a) else 0) + b[j]
        
        # Recurse with the next element in array 'b'
        recursiveSum(i, j + 1, a, b, total_sum)