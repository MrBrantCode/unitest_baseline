"""
QUESTION:
Dominos Pizza has hungry customers waiting in the queue. Each unique order is placed by a customer at time x[i], and the order takes y[i] units of time to complete.
You have information on all n orders, Find the order in which all customers will receive their pizza and return it. If two or more orders are completed at the same time then sort them by non-decreasing order number.
Example 1:
Input : arr[ ] = {{4,1}, {6,2}, {7,6}, 
                       {8,1}, {1,3}}
Output : 5 1 2 4 3
Explanation:
Here an array can be transform to 
{5, 8, 13, 9, 4}. Here 5^{th} index order 
received first then 1^{st} order, 2^{nd} order...
return {5, 1, 2, 4, 3}
Example 2:
Input : arr[ ] = {{1,1}, {1,1}, {1,1}} 
Output :  1 2 3 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function permute() that takes 2-d array (arr), sizeOfArray (n), and return the array of order in which customers will receive their pizza. The driver code takes care of the printing.
Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ arr[i][0], arr[i][1] ≤ 10^{5}
"""

def get_pizza_order(arr, n):
    # Create a list to store the completion times and original indices
    completion_times = []
    
    # Calculate the completion time for each order and store it with its original index
    for i in range(n):
        order_time, prep_time = arr[i]
        completion_times.append((order_time + prep_time, i + 1))
    
    # Sort the orders based on completion time and original index
    completion_times.sort()
    
    # Extract the original indices in the sorted order
    result = [index for _, index in completion_times]
    
    return result