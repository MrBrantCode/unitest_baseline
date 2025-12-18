"""
QUESTION:
Chef has an array of N integers. He wants to play a special game. In this game he needs to make all the integers in the array greater than or equal to 0. 
Chef can use two types of operations. The first type is to  increase all the integers of the given array by 1, but it costs X coins. The operation of the second type is to add 1 to only one integer of the given array and to use this operation you need to pay 1 coin. You need to calculate the minimal cost to win this game (to make all integers greater than or equal to 0)  

-----Input-----

The first line of the input contains an integer N denoting the number of elements in the given array. The second line contains N space-separated integers A1, A2, ..., AN denoting the given array. The third line contains number X - cost of the first type operation. 


-----Output-----
For each test case, output a single line containing minimal cost required to make all the integers greater than or equal to zero.

-----Constraints-----

- 1 ≤ N ≤ 105
- -109 ≤ Ai ≤  109 
- 0 ≤ X  ≤ 109

-----Example-----
Input:
3
-1 -2 -3
2

Output:
5

-----Explanation-----
Example case 1: Use the first type operation twice and the second type once.
"""

def calculate_minimal_cost(N, A, X):
    # Filter out the negative integers
    negative_integers = [i for i in A if i < 0]
    
    # Sort the negative integers in ascending order
    negative_integers.sort()
    
    # Calculate the total cost if we use the first type operation for all negative integers
    total_cost_first_type = -sum(negative_integers)
    
    # If the total cost of the first type operation is less than or equal to X, return it
    if total_cost_first_type <= X:
        return total_cost_first_type
    
    # Otherwise, calculate the cost by using the first type operation for the first X negative integers
    # and the second type operation for the rest
    return -sum(negative_integers[:X])