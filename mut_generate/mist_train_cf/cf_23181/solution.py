"""
QUESTION:
Write a MapReduce function `calculate_average_age` that calculates the average age of users in a dataset. The function should exclude users who are below the age of 18 from the calculation. The function should accept an iterable of user records as input, where each record is a dictionary containing the fields 'user_id', 'name', 'age', 'gender', and 'location'. The function should return a single value representing the average age of the users above 18.
"""

def calculate_average_age(user_records):
    """
    Calculate the average age of users in a dataset using MapReduce.
    
    Args:
    user_records (iterable): An iterable of user records where each record is a dictionary containing the fields 'user_id', 'name', 'age', 'gender', and 'location'.
    
    Returns:
    float: The average age of the users above 18.
    """
    
    # Map phase
    mapped_records = []
    for record in user_records:
        age = record['age']
        mapped_records.append(("key", (age, age >= 18)))
    
    # Reduce phase
    total_age = 0
    count = 0
    for _, value in mapped_records:
        age, flag = value
        if flag:
            total_age += age
            count += 1
    
    # Finalize phase
    if count == 0:
        return 0  # or any other default value when there are no users above 18
    average_age = total_age / count
    return average_age