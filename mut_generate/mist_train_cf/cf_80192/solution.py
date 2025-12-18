"""
QUESTION:
Design a function `book_distribution(current_distribution_list, total_cost, book_types, book_prices)` that takes a list of strings showing the current distribution of books in a library, the total cost of books, a list of book names, and a dictionary containing the prices of each book. The function should return a dictionary revealing the quantity of each book not listed in the initial distribution list, calculated using the price and total cost. The result dictionary should only contain books with a non-zero count.
"""

def book_distribution(current_distribution_list, total_cost, book_types, book_prices):
    # Parse types of books and their quantities from the distribution list and save in the initial_quantity dictionary.
    initial_quantity = {book.split()[1]: int(book.split()[0]) for book in current_distribution_list}

    # Calculate the current cost
    current_cost = sum([book_prices[book_type] * quantity for book_type, quantity in initial_quantity.items()])
    
    # Subtract current cost from total cost
    remaining_cost = total_cost - current_cost

    # Initialize an empty dictionary for the final result
    final_distribution = {}

    # Calculate the quantity of each type of book not listed initially based on the remaining cost
    for book_type in book_types:
        if book_type not in initial_quantity:
            quantity = remaining_cost // book_prices[book_type]
            if quantity > 0:
                final_distribution[book_type] = quantity
                remaining_cost -= quantity * book_prices[book_type]
    
    # Return the final_distribution dictionary which contains the quantity of each book type not listed initially.
    return final_distribution