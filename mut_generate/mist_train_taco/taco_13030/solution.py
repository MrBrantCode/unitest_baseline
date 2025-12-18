"""
QUESTION:
Auction

square1001 You were watching a certain auction.

An auction is a transaction in which when there are a large number of buyers and the number of items is limited, the one with the highest price is given the right to buy. (From the 7th edition of the Shinmei Kokugo Dictionary)

The rules of the auction here are as follows.




1. Repeat steps 2 to 6 below until the item is exhausted.

2. Bring out new items and show them to customers

3. One of the customers puts the item at the price they like

4. Price higher than the price currently on the item by one of the customers

5. Repeat step 4 until there are no more customers to perform the action of 4.

6. The customer who puts the highest price on the item wins the bid




square1001 You recorded all the prices attached to the items during this auction in chronological order.

According to the record, $ N $ items are priced, starting from the beginning with $ A_1, A_2, A_3, \ dots, A_N $.

E869120 You are wondering how many items were put up for sale in this auction.

square1001 From the list you made, find the minimum and maximum possible number of items for sale in this auction.

input

Input is given from standard input in the following format.


$ N $
$ A_1 $ $ A_2 $ $ A_3 $ $ \ cdots $ $ A_N $


output

Please output the minimum and maximum possible number of items listed in this auction in this order, separated by line breaks.

However, insert a line break at the end.

Constraint

* $ 1 \ leq N \ leq 100000 \ (= 10 ^ 5) $
* $ 1 \ leq A_i \ leq 1000000000 \ (= 10 ^ 9) $
* All inputs are integers.



Input example 1


Five
8 6 9 1 20


Output example 1


3
Five


When three items are sold in order at price 8, price 9, and price 20, the minimum number of items is 3.

Input example 2


6
3 3 4 3 3 4


Output example 2


Four
6


Input example 3


8
5 5 4 4 3 3 2 2


Output example 3


8
8






Example

Input

5
8 6 9 1 20


Output

3
5
"""

def calculate_auction_items(prices):
    n = len(prices)
    min_items = 1
    
    for i in range(n - 1):
        if prices[i + 1] <= prices[i]:
            min_items += 1
    
    max_items = n
    
    return min_items, max_items