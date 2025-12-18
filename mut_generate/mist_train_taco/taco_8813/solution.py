"""
QUESTION:
You are given an array arr of N integers representing a min Heap. The task is to convert it to max Heap.
A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node. 
Example 1:
Input:
N = 4
arr = [1, 2, 3, 4]
Output:
[4, 2, 3, 1]
Explanation:
The given min Heap:
          1
        /   \
      2       3
     /
   4
Max Heap after conversion:
         4
       /   \
      3     2
    /
   1
Example 2:
Input:
N = 5
arr = [3, 4, 8, 11, 13]
Output:
[13, 11, 8, 3, 4]
Explanation:
The given min Heap:
          3
        /   \
      4      8
    /   \ 
  11     13
Max Heap after conversion:
          13
        /    \
      11      8
    /   \ 
   3     4
 
Your Task:
Complete the function int convertMinToMaxHeap(), which takes integer N and array represented minheap as input and converts it to the array representing maxheap. You don't need to return or print anything, modify the original array itself.
Note: Only an unique solution is possible under the expected time complexity.
Expected Time Complexity: O(N * log N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^{5}
1 <= arr[i] <= 10^{9}
"""

def convert_min_heap_to_max_heap(arr, N=None):
    """
    Converts a given min-heap represented by an array into a max-heap.

    Parameters:
    - arr (list of int): The array representing the min-heap.
    - N (int, optional): The size of the array. If not provided, it is inferred from the length of `arr`.

    Returns:
    - None: The function modifies the input array `arr` in place.
    """
    if N is None:
        N = len(arr)

    def heapify(arr, i, N):
        largest = i
        l_child = 2 * i + 1
        r_child = 2 * i + 2
        if l_child < N and arr[largest] < arr[l_child]:
            largest = l_child
        if r_child < N and arr[largest] < arr[r_child]:
            largest = r_child
        if largest != i:
            (arr[largest], arr[i]) = (arr[i], arr[largest])
            heapify(arr, largest, N)

    for i in range(N - 1, -1, -1):
        heapify(arr, i, N)