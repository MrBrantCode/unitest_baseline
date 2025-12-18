"""
QUESTION:
Write a MapReduce program that calculates the total number of purchases made by customers who have spent more than $500. The input data consists of key-value pairs where each key represents a customer and the corresponding value represents their purchase amount. The program should also include error handling to account for any invalid data inputs. 

The MapReduce program should consist of two main functions: a mapper function that takes input key-value pairs, checks if the purchase amount is greater than $500, and emits a key-value pair with the customer as the key and a value of 1 if the condition is met; and a reducer function that takes the output of the mapper, performs a summation for each customer, and emits a final key-value pair with the customer as the key and the total number of purchases as the value.
"""

def purchases_over_500(customer_purchase):
    """
    Calculate the total number of purchases made by customers who have spent more than $500.
    
    Args:
        customer_purchase (dict): A dictionary containing customer-purchase amount key-value pairs.
    
    Returns:
        dict: A dictionary with customers as keys and their total number of purchases as values.
    """
    
    # Initialize an empty dictionary to store the total purchases for each customer
    total_purchases = {}
    
    # Iterate through each customer-purchase pair
    for customer, purchase_amount in customer_purchase.items():
        try:
            # Check if the purchase amount is greater than $500
            if purchase_amount > 500:
                # If the customer is already in the dictionary, increment their purchase count
                if customer in total_purchases:
                    total_purchases[customer] += 1
                # Otherwise, add the customer to the dictionary with a purchase count of 1
                else:
                    total_purchases[customer] = 1
        except Exception as e:
            # Handle invalid data inputs by printing an error message
            print('Invalid input: ' + str(e), file=sys.stderr)
    
    return total_purchases