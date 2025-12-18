"""
QUESTION:
You have records of employee name as string (E_{name}) and salary as positive integer (S). You have to sort the records on the basis of employee salary, if salary is same then use employee name for comparison.
Example 1:
Input: N = 2
arr[] = {{xbnnskd, 100}, {geek, 50}}
Output: {geek 50}, {xbnnskd 100}
Explanation: geek has lowest salary 
as 50 and xbnnskd has more salary.
Example 2: 
Input: N = 2
arr[] = {{shyam, 50}, {ram, 50}} 
Output: ram 50 shyam 50
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function sortRecords() that takes array arr[] and integer N as parameters and sort the array according to the above-given conditions. The function does not return anything.
 
Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{3}
"""

def sort_employee_records(arr, N):
    """
    Sorts the list of employee records based on salary and employee name.

    Parameters:
    arr (list of tuples): A list of tuples where each tuple contains an employee name (string) and their salary (positive integer).
    N (int): The number of records in the list.

    Returns:
    None: The function sorts the input list in place.
    """
    arr.sort(key=lambda x: (x[1], x[0]))