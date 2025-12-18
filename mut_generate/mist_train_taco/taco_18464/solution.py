"""
QUESTION:
Akku have solved many problems, she is genius. One day her friend gave her an Array of size n and asked her to perform
some queries of following type:
Each query consists of three integers
1 A B : Update the Array at index A by value B
2 A B : if the subarray from index A to B (both inclusive) is
        1. Both increasing(Non-decreasing) and decreasing(Non-increasing) print -1
        2. Only increasing(Non-decreasing) print 0
        3. Only decreasing(Non-increasing) print 1
        4. Neither increasing nor decreasing print -1
Akku needs your help, can you help her.
 
Example 1:
Input: nums = {1,5,7,4,3,5,9},
Queries = {{2,1,3},{1,7,4},{2,6,7}}
Output: {0,1}
Explanation: For the 1st query given :
A = 1, B = 3. From 1 to 3(1,5,7) elements 
are in increasing order. So answer is 0.
For the 2nd query we have to update the 7th
element of the array by 4. So new updated array
will be {1,5,7,4,3,5,4}
For the 3rd query A = 6, B = 7. From 6 to 7
(5, 4) elements are in descending order. So 
answer is 1.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function solveQueries() which takes nums and Queries as input parameter and returns a list containing the answer for the 2nd type of query.
 
Expected Time Comeplxity: O(n*log(n))
Expected Space Comeplxity: O(n)
 
Constraints:
1 <= n <= 10^{4}
1 <= nums[i] <= 10^{4}
1 <= No. of queries <= 10^{4}
"""

def solve_queries(nums, queries):
    def is_increasing(subarray):
        return all(subarray[i] <= subarray[i + 1] for i in range(len(subarray) - 1))
    
    def is_decreasing(subarray):
        return all(subarray[i] >= subarray[i + 1] for i in range(len(subarray) - 1))
    
    results = []
    
    for query in queries:
        query_type, A, B = query
        if query_type == 1:
            # Update the array at index A with value B
            nums[A - 1] = B
        elif query_type == 2:
            # Determine the nature of the subarray from index A to B
            subarray = nums[A - 1:B]
            if is_increasing(subarray) and is_decreasing(subarray):
                results.append(-1)
            elif is_increasing(subarray):
                results.append(0)
            elif is_decreasing(subarray):
                results.append(1)
            else:
                results.append(-1)
    
    return results