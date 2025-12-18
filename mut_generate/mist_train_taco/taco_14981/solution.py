"""
QUESTION:
You need to swap the head and the tail of the specified array:

the head (the first half) of array moves to the end, the tail (the second half) moves to the start. 
The middle element (if it exists) leaves on the same position.

Return new array.


 For example:
 ```
    [ 1, 2, 3, 4, 5 ]   =>  [ 4, 5, 3, 1, 2 ]
     \----/   \----/         
      head     tail 
 
    [ -1, 2 ]  => [ 2, -1 ] 
    [ 1, 2, -3, 4, 5, 6, -7, 8 ]   =>  [ 5, 6, -7, 8, 1, 2, -3, 4 ]  
```
"""

def swap_head_tail(a: list) -> list:
    """
    Swaps the head and tail of the specified array.
    
    The head (the first half) of the array moves to the end, and the tail (the second half) moves to the start.
    The middle element (if it exists) remains in the same position.
    
    Parameters:
    a (list): The input array to be modified.
    
    Returns:
    list: The modified array with the head and tail swapped.
    """
    r = (len(a) + 1) // 2
    l = len(a) // 2
    return a[r:] + a[l:r] + a[:l]