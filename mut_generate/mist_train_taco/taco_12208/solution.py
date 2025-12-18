"""
QUESTION:
Mr. Geek is a greedy seller. He has a stock of N laptops which comprises of both useful and useless laptops. Now, he wants to organize a sale to clear his stock of useless laptops. The prices of N laptops are A_{i }each consisting of positive and negative integers (-ve denoting useless laptops). In a day, he can sell atmost M laptops. Mr. Geek being a greedy seller want to earn maximum profit out of this sale. So, help him maximizing his profit by selling useless laptops.
 
Example 1:
Input:
N=4, M=3
A[] = {-6, 0, 35, 4}
Output:
6
Explanation:
Geek sells the laptops with price -6 and
earns Rs. 6 as profit.
 
Example 2:
Input:
N=5, M=10
A[] = {1, -2, -3, -4, 5}
Output:
9
Explanation:
Geek sells the laptops with price -2,
-3 and -4 and earns Rs. 9 as profit.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxProfit() which takes the array A[], its size N and an integer M as inputs and returns the maximum profit Mr. Geek can earn in a single day.
 
Expected time Complexity: O(NlonN)
Expected time Complexity: O(1)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ M ≤ 10^{5}
-10^{6 }≤ A_{i} ≤ 10^{6}
"""

def maxProfit(A, N, M):
    # Extract the prices of useless laptops (negative prices)
    useless_laptops = [price for price in A if price < 0]
    
    # Sort the useless laptops by price (ascending order)
    useless_laptops.sort()
    
    # Initialize total profit and count of laptops sold
    total_profit = 0
    laptops_sold = 0
    
    # Iterate through the sorted useless laptops and calculate profit
    for laptop_price in useless_laptops:
        if laptops_sold < M:
            total_profit += laptop_price
            laptops_sold += 1
        else:
            break
    
    # Return the negative of total profit (since profit is negative for useless laptops)
    return -total_profit