"""
QUESTION:
You are given three integers A, B and C. Find the minimum number of operations required to make A, B and C all equal by repeatedly performing the following two kinds of operations in any order:
 - Choose two among A, B and C, then increase both by 1.
 - Choose one among A, B and C, then increase it by 2.
It can be proved that we can always make A, B and C all equal by repeatedly performing these operations.

-----Constraints-----
 - 0 \leq A,B,C \leq 50
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B C

-----Output-----
Print the minimum number of operations required to make A, B and C all equal.

-----Sample Input-----
2 5 4

-----Sample Output-----
2

We can make A, B and C all equal by the following operations:
 - Increase A and C by 1. Now, A, B, C are 3, 5, 5, respectively.
 - Increase A by 2. Now, A, B, C are 5, 5, 5, respectively.
"""

def min_operations_to_equalize(A, B, C):
    # Create a list from the input values
    numbers = [A, B, C]
    
    # Sort the list in descending order
    numbers.sort(reverse=True)
    
    # Initialize the answer variable
    ans = 0
    
    # Calculate the difference between the largest and the second largest
    ans += numbers[0] - numbers[1]
    
    # Adjust the second and third numbers to match the largest
    numbers[1] += ans
    numbers[2] += ans
    
    # Calculate the remaining operations needed to make all three equal
    ans += (numbers[0] - numbers[2]) // 2
    ans += (numbers[0] - numbers[2]) % 2 * 2
    
    return ans