"""
QUESTION:
Implement a recursive function `get_names` that takes a list of dictionaries as input, where each dictionary represents an individual with a 'name' and an 'age'. The function should return a list of names of individuals whose age is greater than 25 and whose names contain the letter 'a'. The time complexity of the function should be O(n), where n is the number of individuals in the data.
"""

def get_names(data):
    # Base case: if the data is empty, return an empty list
    if not data:
        return []
    
    # Recursive case: check the first individual in the data
    individual = data[0]
    
    # Check if the individual's age is greater than 25 and their name contains the letter 'a'
    if individual['age'] > 25 and 'a' in individual['name'].lower():
        # If the conditions are met, add their name to the result list
        result = [individual['name']]
    else:
        result = []
    
    # Recursively call the function on the remaining individuals in the data
    result += get_names(data[1:])
    
    return result