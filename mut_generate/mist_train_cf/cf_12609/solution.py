"""
QUESTION:
Write a function named calculate_trip_cost that calculates the total cost of a trip given the cost and quantity of hotel rooms for each day of the week, with the following conditions:
- The cost and quantity of hotel rooms for each day of the week are retrieved from separate lists.
- The total cost should only include weekdays (Monday to Friday) and exclude weekends (Saturday and Sunday).
 
The input parameters should include two lists: one for the costs of hotel rooms for each day of the week and one for the quantity of hotel rooms for each day of the week.
"""

def calculate_trip_cost(costs, quantities):
    total_cost = 0
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for i in range(len(costs)):
        day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i % 7]
        
        if day in weekdays:
            total_cost += costs[i] * quantities[i]
    
    return total_cost