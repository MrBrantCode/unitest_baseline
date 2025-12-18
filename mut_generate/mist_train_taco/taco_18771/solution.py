"""
QUESTION:
Shil, Aditya and Utkarsh go to a candy shop. There are N candies present in the shop, which are indexed from 1 to N. All three of them select one candy to eat.

However, a candy tastes delicious if and only if, the index of candy chosen by Shil is strictly less than the index of candy chosen by Aditya and the index of candy chosen by Aditya is strictly greater than index of candy chosen by Utkarsh. 

To state in simple Mathematical terms, if Shil chooses i^th candy, Aditya chooses j^th candy and Utkarsh chooses k^th candy, then the candies would taste delicious 
if and only if i < j and j > k.
You have to find the total number of ways in which they can choose candies such that the candies would taste delicious to them. Note that all of them choose distinct number of candies i.e.,  i!=j and j!=k and i!=k.

Input format:
The only line of input consists of a single integer N denoting the total number of candies.   

Output format:
Find the total number of ways by which all three can choose candies such that the candies would taste delicious to them.  

Constraints:
3 ≤ N ≤ 1000

SAMPLE INPUT
4

SAMPLE OUTPUT
8

Explanation

All the possible ways to choose candies are:  
[1,3,2]  
[2,3,1]  
[2,4,3]  
[3,4,2]  
[1,4,3]  
[3,4,1]  
[2,4,1]  
[1,4,2]  

The first integer in all the tuples denotes index of candy chosen by Shil, the second integer denotes index of candy chosen by Aditya and the third integer denotes index of candy chosen by Utkarsh.
"""

def count_delicious_candy_ways(n: int) -> int:
    """
    Calculate the total number of ways Shil, Aditya, and Utkarsh can choose candies
    such that the candies would taste delicious.

    The candies taste delicious if:
    - Shil chooses a candy with index i
    - Aditya chooses a candy with index j
    - Utkarsh chooses a candy with index k
    and the conditions i < j and j > k are satisfied.

    Parameters:
    n (int): The total number of candies.

    Returns:
    int: The total number of ways to choose the candies.
    """
    if n < 3:
        return 0
    
    # Calculate the number of ways using combinatorial logic
    ways = n * (n - 1) * (n - 2) // 6
    
    return ways