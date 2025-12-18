"""
QUESTION:
Given are the heights of certain Buildings which lie adjacent to each other. Sunlight starts falling from the left side of the buildings. If there is a building of a certain Height, all the buildings to the right side of it having lesser heights cannot see the sun. The task is to find the total number of such buildings that receive sunlight.
 
Example 1:
Input:
N = 6
H[] = {6, 2, 8, 4, 11, 13}
Output:
4
Explanation:
Only buildings of height 6, 8, 11 and
13 can see the sun, hence output is 4.
 
Example 2:
Input:
N = 5
H[] = {2, 5, 1, 8, 3}
Output:
3
Explanation:
Only buildings of height 2, 5 and 8
can see the sun, hence output is 3.
 
Example 3:
Input:
N = 7
H[] = {3, 4, 1, 0, 6, 2, 3}
Output:
3
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function longest() which takes the array A[] and its size N as inputs and returns the desired output.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ H_{i} ≤ 10^{5}
"""

def count_buildings_with_sunlight(heights, n):
    if n == 0:
        return 0
    
    max_height = heights[0]
    count = 1
    
    for i in range(1, n):
        if heights[i] >= max_height:
            max_height = heights[i]
            count += 1
    
    return count