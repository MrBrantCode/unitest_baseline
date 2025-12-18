"""
QUESTION:
Distribute a variable number of products among a variable number of warehouses. Write a function `distribute_products(w, p)` where `w` is the number of warehouses (10 to 10000), and `p` is the number of products (10000 to 10000000). The function should return a list where each element represents the number of products in each warehouse, distributed as evenly as possible. If `p` cannot be evenly divided by `w`, the remaining products should be allocated in a round-robin fashion to the warehouses. The function should be efficient for large inputs.
"""

def entrance(w, p):
    assert(w > 0)
    
    # calculate base number of products per warehouse
    base_products = p // w
    # calculate remaining products to distribute
    remaining_products = p % w

    # create a list where each element represents a warehouse,
    # and the value is the number of products in the warehouse
    warehouses = [base_products] * w

    # distribute remaining products in a round-robin fashion
    for i in range(remaining_products):
        warehouses[i] += 1

    return warehouses