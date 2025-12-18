"""
QUESTION:
For a given number N. Print the pattern in the following form: 1 121 12321 1234321 for N = 4.
Example 1:
Input:
N = 3
Output:
1 121 12321
Explanation:
For N = 3 we will print the 3 strings 
according to the pattern.
Example 2:
Input:
N = 6
Output:
1 121 12321 1234321 123454321 12345654321
Explanation:
For N = 6 we will print the 6 strings 
according to the pattern.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function numberPattern() which takes an integer N as input parameter and returns the list of strings to be printed.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 200
"""

def generate_number_pattern(N: int) -> list[str]:
    result = []
    for i in range(1, N + 1):
        # Generate the increasing part of the pattern
        increasing_part = ''.join(str(j) for j in range(1, i + 1))
        # Generate the decreasing part of the pattern
        decreasing_part = ''.join(str(j) for j in range(i - 1, 0, -1))
        # Combine both parts and add to the result list
        result.append(increasing_part + decreasing_part)
    return result