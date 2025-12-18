"""
QUESTION:
Create a function named 'delete_records' that deletes records from a table based on given conditions. The function should take two parameters: the table name and the field name to delete records with a given value. The function should only delete records if the 'salary' is greater than 50000, 'experience' is less than 5, 'age' is between 25 and 40, 'education' is either "Bachelor's" or "Master's", 'location' is within a given list of allowed locations, and 'position' is not "Manager" or "Director".
"""

def delete_records(tableName, fieldName):
    query = f"""
        DELETE FROM {tableName}
        WHERE salary > 50000
          AND experience < 5
          AND age >= 25 AND age <= 40
          AND education IN ("Bachelor's", "Master's")
          AND location IN ("Location1", "Location2", "Location3")
          AND position NOT IN ("Manager", "Director")
    """
    return query