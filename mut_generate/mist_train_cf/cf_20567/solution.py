"""
QUESTION:
Create a function called `permute(arr, start, end)` to print all permutations of an input array in lexicographically sorted order, without using any additional memory space. The function should have a time complexity of O(n!), where n is the length of the input array. The input array is passed as `arr`, and `start` and `end` are indices representing the current subarray being permuted.
"""

def permute(arr, start, end):
    if start == end:
        print(arr)
        return
    
    for i in range(start, end+1):
        # Swap current element with the first element
        arr[start], arr[i] = arr[i], arr[start]
        
        # Recursively generate permutations for the remaining elements
        permute(arr, start+1, end)
        
        # Swap back to restore the original array
        arr[start], arr[i] = arr[i], arr[start]