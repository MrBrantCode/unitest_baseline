"""
QUESTION:
Pappu is confused between 6 & 9. He works in the billing department of abc company and his work is to return the remaining amount to the customers. If the actual remaining amount is given we need to find the maximum possible extra amount given by the pappu to the customers.
Example 1:
Input: amount = 56
Output: 3
Explanation: maximum possible extra 
             amount = 59 - 56 = 3.
Example 2:
Input: amount = 66
Output: 33
Explanation: maximum possible extra 
             amount = 99 - 66 = 33.
User Task:
Your task is to complete the function findDiff() which takes single argument(amount) and returns the answer. You need not take any input or print anything.
Expected Time Complexity: O(log_{10}amount).
Expected Auxiliary Space: O(log_{10}amount).
Constraints
1 ≤ N≤ 10000001
"""

def calculate_max_extra_amount(amount: int) -> int:
    # Convert the amount to a string to manipulate individual digits
    str_amount = str(amount)
    
    # Create a new string where all '6's are replaced with '9's
    max_amount_str = ''.join('9' if char == '6' else char for char in str_amount)
    
    # Convert the new string back to an integer
    max_amount = int(max_amount_str)
    
    # Calculate the difference between the maximum possible amount and the actual amount
    extra_amount = max_amount - amount
    
    return extra_amount