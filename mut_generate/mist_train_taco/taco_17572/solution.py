"""
QUESTION:
Given a row wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.
Example 1:
Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]
Output: 5
Explanation: Sorting matrix elements gives 
us {1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 
 
Example 2:
Input:
R = 3, C = 1
M = [[1], [2], [3]]
Output: 2
Explanation: Sorting matrix elements gives 
us {1,2,3}. Hence, 2 is median.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function median() which takes the integers R and C along with the 2D matrix as input parameters and returns the median of the matrix.
Expected Time Complexity: O(32 * R * log(C))
Expected Auxiliary Space: O(1)
Constraints:
1 <= R, C <= 400
1 <= matrix[i][j] <= 2000
"""

def find_matrix_median(matrix, R, C):
    # Flatten the matrix into a single list
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    
    # Sort the flattened list
    flat_list.sort()
    
    # Calculate the median
    mid_index = len(flat_list) // 2
    if len(flat_list) % 2 == 0:
        # If even number of elements, return the average of the two middle elements
        return (flat_list[mid_index] + flat_list[mid_index - 1]) / 2
    else:
        # If odd number of elements, return the middle element
        return flat_list[mid_index]