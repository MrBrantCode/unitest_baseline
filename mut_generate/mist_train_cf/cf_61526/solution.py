"""
QUESTION:
Given three types of cookies priced at $2, $3, and $4 each, and total purchases of 12 cookies for $32, find the number of each type of cookie bought, with each type being bought at least once, using the function `find_cookies(x, y, z, total_cookies, total_spent)`.
"""

def find_cookies(total_cookies, total_spent):
    # Initialize variables to store the result
    x, y, z = 0, 0, 0
    
    # Try all combinations of x, y, z that add up to total_cookies
    for x in range(1, total_cookies):
        for y in range(1, total_cookies - x):
            z = total_cookies - x - y
            
            # Check if the current combination satisfies the total cost
            if 2 * x + 3 * y + 4 * z == total_spent:
                return x, y, z
    
    # If no combination is found, return None
    return None