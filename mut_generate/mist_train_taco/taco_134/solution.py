"""
QUESTION:
$Harshad$ $Mehta$ is planning  a new scam with the stocks he is given a stock of  integer price S and a number K . $harshad$ has got the power to change the number $S$ at most $K$ times
In order to raise the price of stock and now cash it for his benefits
Find the largest price at which $harshad$ can sell the stock in order to maximize his profit 

-----Input:-----
- First line will contain $S$ and  $K$ , the price of the stock and the number K 

-----Output:-----
Print the largest profit  he can make in a single line.

-----Constraints-----
- S can take value upto 10^18
NOTE: use 64 int number to fit range
- K can take value from [0.. 9]

-----Sample Input:-----
4483 2

-----Sample Output:-----
9983

-----EXPLANATION:-----
First two digits of the number are changed to get the required number.
"""

def maximize_stock_price(S: int, K: int) -> int:
    if K == 0:
        return S
    
    # Convert the stock price to a list of characters
    digits = list(str(S))
    
    # Iterate over the digits and change them to '9' if possible
    for i in range(len(digits)):
        if K == 0:
            break
        if digits[i] != '9':
            digits[i] = '9'
            K -= 1
    
    # Join the list back into a string and convert to integer
    max_price = int(''.join(digits))
    
    return max_price