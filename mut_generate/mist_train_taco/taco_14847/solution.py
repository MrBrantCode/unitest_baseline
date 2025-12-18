"""
QUESTION:
Given two positive integers N and X, where N is the number of total patients and X is the time duration(in minutes) after which a new patient arrives. Also, doctor will give only 10 minutes to each patient. The task is to calculate the time (in minutes) the last patient needs to wait.
Example 1:
Input: N = 4, X = 5
Output: 15
Explaination: The arrival time of the 
patients are 0, 5, 10 and 15 respectively. 
The times when the first three patients 
are checked are respectively 10, 20, 30. 
So the Waiting time is 30 - 15 = 15.
Example 2:
Input: N = 3, X = 10
Output: 0
Explaination: The incoming time of the 
patients are 0, 10 and 20 and the firts 
two patients are finished checking at 10, 
20. So the last patient does not need to 
wait.
Your Task:
You do not need to read input or print anything. Your task is to complete the function waitingTime() which takes N and X as input parameters and returns the waiting time of the last patient.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 100
1 ≤ X ≤ 30
"""

def calculate_waiting_time(N: int, X: int) -> int:
    """
    Calculate the waiting time of the last patient.

    Parameters:
    - N (int): The number of total patients.
    - X (int): The time duration (in minutes) after which a new patient arrives.

    Returns:
    - int: The waiting time (in minutes) of the last patient.
    """
    waiting_time = (N - 1) * 10 - X * (N - 1)
    return max(waiting_time, 0)