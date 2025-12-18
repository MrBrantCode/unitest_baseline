"""
QUESTION:
Write a function to filter customer records based on specific criteria. The function should return all records where the state is "California", the phone number starts with "555", and the last name starts with the letter "S".
"""

def filter_customers(customers):
    """
    Filter customer records based on specific criteria.
    
    Args:
        customers (list of dict): List of customer records.
        
    Returns:
        list of dict: Filtered customer records.
    """
    return [customer for customer in customers 
            if customer['state'] == "California" 
            and customer['phone_number'].startswith("555") 
            and customer['last_name'].startswith("S")]