"""
QUESTION:
Implement a function `bottomUpCutRod(prices, n)` that takes a list of prices and an integer n as input, where the list of prices represents the maximum revenue for each length of rod and n is the length of the rod. The function should return the maximum revenue that can be obtained by cutting up the rod. The function should use dynamic programming and fill up a table in a bottom-up manner.
"""

def cutRod(prices, n): 
    # Create an array of size n+1 
    temp_array = [0 for i in range(n+1)] 
    for i in range(1, n+1): 
        tempval = -float('inf') 
        for j in range(i): 
            tempval = max(tempval, prices[j] + temp_array[i-j-1]) 
        temp_array[i] = tempval 
  
    return temp_array[n]