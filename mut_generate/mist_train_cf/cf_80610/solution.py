"""
QUESTION:
Design a data transmission infrastructure that captures and processes consumer activity metadata from an online retail platform using Apache Flink. The infrastructure should read data from RabbitMQ, manipulate it to outline consumer purchasing behavior, and then write the results to Amazon Redshift.

Implement a function named `process_func` that takes raw data as input and returns the manipulated data outlining consumer purchasing behavior. 

Note: You should implement or use existing RabbitMQ and Redshift connectors/adapters, and ensure that you have the necessary libraries and environment setup before implementing the function.
"""

def process_func(data):
    # Assuming data is a dictionary containing user_id, item_id, purchase_time, and purchase_amount.
    # You may need to adjust this based on the actual format of your data.

    # Manipulate the raw data to outline consumer purchasing behavior
    # For example, you can calculate the total purchase amount for each user
    user_purchases = {}
    for purchase in data:
        user_id = purchase['user_id']
        if user_id not in user_purchases:
            user_purchases[user_id] = 0
        user_purchases[user_id] += purchase['purchase_amount']

    # Create a new list of dictionaries with the manipulated data
    manipulated_data = []
    for user_id, total_purchase_amount in user_purchases.items():
        manipulated_data.append({
            'user_id': user_id,
            'total_purchase_amount': total_purchase_amount
        })

    return manipulated_data