"""
QUESTION:
Given a number N. Your task is to check whether it is fascinating or not.
Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3, and when both these products are concatenated with the original number, then it results in all digits from 1 to 9 present exactly once.
Example 1:
Input: 
N = 192
Output: Fascinating
Explanation: After multiplication with 2
and 3, and concatenating with original
number, number will become 192384576 
which contains all digits from 1 to 9.
Example 2:
Input: 
N = 853
Output: Not Fascinating
Explanation: It's not a fascinating
number.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function fascinating() which takes the integer n parameters and returns boolean(True or False) denoting the answer.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
100 <= N <= 2*10^{9}
"""

def is_fascinating(n: int) -> bool:
    # Check if the number has 3 or more digits
    if n < 100:
        return False
    
    # Calculate the products
    f = n * 2
    s = n * 3
    
    # Concatenate the original number, and its products
    concatenated_str = str(n) + str(f) + str(s)
    
    # Convert the concatenated string to a sorted list of characters
    sorted_digits = sorted(concatenated_str)
    
    # Check if the sorted list matches the list of digits from 1 to 9
    return sorted_digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']