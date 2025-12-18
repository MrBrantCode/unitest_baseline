"""
QUESTION:
Given an array arr[] which contains data of N nodes of Complete Binary tree in level order fashion. The task is to print the level order traversal in sorted order. 
Example 1:
Input:
N = 7
arr[] = {7 6 5 4 3 2 1}
Output:
7
5 6
1 2 3 4
Explanation: The formed Binary Tree is:
             7
          /      \
        6         5
      /  \      /   \
     4    3    2     1
Example 2:
Input:
N = 6
arr[] = {5 6 4 9 2 1}
Output:
5
4 6
1 2 9
Explanation: The formed Binary Tree is:
             5
          /     \
        6        4
      /  \      /    
     9    2    1    
Your Task:
You don't need to read input or print anything. Your task is to complete the function binTreeSortedLevels() which takes the array arr[] and its size N as inputs and returns a 2D array where the i-th array denotes the nodes of the i-th level in sorted order.
Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10^{4}
"""

def binTreeSortedLevels(arr, n):
    li = []
    i = 0
    level = 0
    while i < n:
        dumm = []
        if level == 0:
            li.append([arr[i]])
            i += 1
            level += 1
        else:
            size = 2 ** level
            if i + size < n:
                dumm.extend(arr[i:i + size])
                dumm.sort()
                li.append(dumm)
                i += size
                level += 1
            else:
                dumm.extend(arr[i:])
                dumm.sort()
                li.append(dumm)
                break
    return li