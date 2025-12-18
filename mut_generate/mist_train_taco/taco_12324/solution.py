"""
QUESTION:
You are given an integer N. Print numbers from 1 to N without the help of loops.
Example 1:
Input:
N = 5
Output:
1 2 3 4 5
Explanation:
We have to print numbers from 1 to 5.
Example 2:
Input:
N = 10
Output:
1 2 3 4 5 6 7 8 9 10
Explanation:
We have to print numbers from 1 to 10.
Your Task:  
You don't need to read input. Your task is to complete the function printTillN() which takes an integer N as an input parameter and print numbers from 1 to N space-separated integers without the help of loops.
Note: print newline character at the end.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 1000
"""

def print_numbers_till_n(N: int) -> None:
    """
    Prints numbers from 1 to N (inclusive) without using loops.

    Parameters:
    N (int): The upper limit of the range of numbers to be printed.

    Returns:
    None: The function prints the numbers directly.
    """
    def print_numbers(current: int):
        if current > N:
            return
        print(current, end=' ')
        print_numbers(current + 1)
    
    print_numbers(1)
    print()  # To print a newline at the end