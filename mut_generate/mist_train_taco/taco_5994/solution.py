"""
QUESTION:
As it is the Valentines month,  Puchi's girlfriend asks him to take her shopping. He, being the average bloke, does not have a lot of money to spend. Hence, decides to buy each item from the shop that offers the best price on it.
His girlfriend wants to buy N items. Each item is available on M shops .
Being the Valentine Season, shops have the products on a discounted price.   But, the discounts are in the form of  successive discounts. Each shop has a successive discount of order-3 on each of the N products.  
Find, for each item, the shop that offers the best price on it.
You may assume that the base price of each item is same on all shops.
Note: 
A successive discount of  25% and 50% on an item of Rs 1000,  means getting a discount of 50% on the new price, after getting a discount of 25% on original price, i.e   item is available at Rs 750 after a 25% discount , and successively at Rs 375 after two successive discounts of 25 and 50.  

Input:
First line contains T the number of test cases. T test cases follow.
First line of each test case contains two space-separated integers  N and M , the number of items and the number of shops respectively. 
 It is followed by description of N products.  Each product description consists of M lines with 3 integers each, the successive discounts offered on that product.

Output:
Print N space separated integers i.e for the i'th  product, print the  index (1 ≤ index ≤ M) of the shop  that offers the best price for that product.
In case of multiple shops offering the same discount, output the one with lower index.  

Constraints: 
1 ≤ N, M ≤ 1000
0 ≤ Discounts ≤ 100

Large I/O files.

SAMPLE INPUT
2
1 3
20 20 50
30 20 0
60 50 0
2 2
20 20 20
30 20 40
10 100 90
35 60 50

SAMPLE OUTPUT
3 
2 1
"""

def find_best_shop_for_items(test_cases):
    results = []
    
    for case in test_cases:
        N = case['N']
        M = case['M']
        discounts = case['discounts']
        
        item_results = []
        
        for item in range(N):
            min_price = float('inf')
            min_shop = 0
            
            for shop in range(M):
                d1, d2, d3 = discounts[item][shop]
                price = 100 * (1 - d1 / 100) * (1 - d2 / 100) * (1 - d3 / 100)
                
                if price < min_price:
                    min_price = price
                    min_shop = shop + 1  # Convert to 1-based index
            
            item_results.append(min_shop)
        
        results.append(item_results)
    
    return results