"""
QUESTION:
You work in the best consumer electronics corporation, and your boss wants to find out which three products generate the most revenue.
Given 3 lists of the same length like these:

* products: `["Computer", "Cell Phones", "Vacuum Cleaner"]`
* amounts: `[3, 24, 8]`
* prices: `[199, 299, 399]`


return the three product names with the highest revenue (`amount * price`).

**Note**: if multiple products have the same revenue, order them according to their original positions in the input list.
"""

def top_three_products_by_revenue(products, amounts, prices):
    # Combine the lists into a list of tuples (product, amount, price)
    combined = list(zip(products, amounts, prices))
    
    # Sort the combined list by revenue (amount * price) in descending order
    sorted_combined = sorted(combined, key=lambda x: x[1] * x[2], reverse=True)
    
    # Extract the top 3 product names
    top_three_products = [item[0] for item in sorted_combined[:3]]
    
    return top_three_products