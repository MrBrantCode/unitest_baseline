"""
QUESTION:
The worlds most successful thief Albert Spaggiari was planning for his next heist on the world bank. He decides to carry a sack with him, which can carry a maximum weight of C kgs. Inside the world bank there were N large blocks of gold. All the blocks have some profit value associated with them i.e. if he steals i^{th} block of weight w[i] then he will have p[i] profit. As blocks were heavy he decided to steal some part of them by cutting them with his cutter.
The thief does not like symmetry, hence, he wishes to not take blocks or parts of them whose weight is a perfect square. Now, you need to find out the maximum profit that he can earn given that he can only carry blocks of gold in his sack. 
Note: The answer should be precise upto 3 decimal places.
Example 1 :
N = 3, C = 10
w[] = {4, 5, 7}
p[] = {8, 5, 4)
Output: 
7.857
Explanation: As first blocks weight is 4
which is a perfect square, he will not use 
this block. Now with the remaining blocks 
the most optimal way is to use 2^{nd} block 
completely and cut 5kg piece from the 3^{rd} 
block to get a total profit of 5 + 2.857 
= 7.857
Your Task:
You don't need to read or print anything. Your task is to complete the function maximumProfit() which takes N, C, w[ ] and p[ ] as input parameters and returns the maximum profit thief can achieve with precision upto 3 decimal places.
Expected Time Complexity: O(N * LogN)
Expected Space Complexity : O(N)
Constraints:
1 ≤ N ≤ 10^{3}
1 ≤ C ≤ 10^{18}
1 ≤ W_{i }≤ 10^{9}
1 ≤ P_{i }≤ 10^{9}
"""

def maximum_profit(N, C, w, p):
    # Create a list of tuples (profit-to-weight ratio, weight, profit)
    arr = sorted([(pi / wi, wi, pi) for (wi, pi) in zip(w, p)], reverse=True)
    
    # Initialize the maximum profit
    ans = 0.0
    
    # Iterate through the sorted list
    for (ri, wi, pi) in arr:
        # Check if the weight is not a perfect square
        if not int(wi ** 0.5) == wi ** 0.5:
            # If the sack can carry the entire block
            if C > wi:
                ans += pi
                C -= wi
            # If the sack can only carry a part of the block
            else:
                ans += round(C * ri, 3)
                break
    
    # Return the maximum profit with precision up to 3 decimal places
    return round(ans, 3)