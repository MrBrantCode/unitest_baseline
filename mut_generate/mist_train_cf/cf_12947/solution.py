"""
QUESTION:
Create a function named `assign_name` that uses the ternary operator to assign a value to `name` based on a complex condition involving at least three variables and at least one logical operator and one comparison operator. The condition should have a complexity of at least O(n), where n is the number of variables involved in the condition.
"""

def assign_name(age, city, salary):
    name = 'John' if (age >= 18 and (city == 'New York' or city == 'San Francisco') and salary >= 50000) else 'Unknown'
    return name