"""
QUESTION:
Write a function `convert_sql_to_python` that takes a list of dictionaries representing student records with 'name' and 'grade' keys. Convert a given SQL query into its equivalent Python expression using list comprehension. The function should return the sorted list of student records in ascending order of the student's name. The SQL query to be converted is not provided, so assume it is a simple SELECT statement to retrieve student records.
"""

def convert_sql_to_python(student_records):
    """
    This function takes a list of dictionaries representing student records, 
    and returns the sorted list of student records in ascending order of the student's name.
    
    Parameters:
    student_records (list): A list of dictionaries containing 'name' and 'grade' keys.
    
    Returns:
    list: The sorted list of student records in ascending order of the student's name.
    """
    
    return sorted(student_records, key=lambda x: x['name'])