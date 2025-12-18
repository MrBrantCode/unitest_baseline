"""
QUESTION:
Create a function named `select_customers(customer_table, zipcode_range)` that filters customers from the `customer_table` based on the conditions that the customer's age is greater than 25 and their zip code falls within the given `zipcode_range`. 

The function should handle corrupted data by defaulting to 25 for non-integer or missing age values, and to the lowest value in `zipcode_range` for non-integer or missing zip code values. 

The function should return a dictionary with the format {"name": [...], "age": [...], "zipcode": [...]}.
"""

def select_customers(customer_table, zipcode_range):
    result = {"name": [], "age": [], "zipcode": []}

    for customer in customer_table:
        try:
            if customer[0] is None:
                continue         
            name = customer[0]

            try:
                age = int(customer[1])
            except (ValueError, TypeError):  
                age = 25

            try:
                zipcode = int(customer[2])
            except (ValueError, TypeError):
                zipcode = zipcode_range[0]

            if age > 25 and zipcode_range[0] <= zipcode <= zipcode_range[1]:
                result["name"].append(name)
                result["age"].append(age)
                result["zipcode"].append(zipcode)
                
        except Exception as e:
            print(f'An error occurred: {e}')
            continue
    
    return result