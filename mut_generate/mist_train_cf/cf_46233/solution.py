"""
QUESTION:
Write a function `get_second_hobby_age` that takes a list of student objects as input. Each student object is a dictionary that contains a key 'hobbies', which is a list of hobby objects. Each hobby object is a dictionary that contains a key 'hobbyAge'. The function should return the 'hobbyAge' of the second hobby of the first student in the list. If the input list is empty or the first student has less than two hobbies, the function should return None.
"""

def get_second_hobby_age(students):
    """
    Returns the 'hobbyAge' of the second hobby of the first student in the list.
    
    Args:
    students (list): A list of student objects.
    
    Returns:
    int or None: The 'hobbyAge' of the second hobby of the first student, or None if the input list is empty or the first student has less than two hobbies.
    """
    
    if len(students) == 0 or len(students[0]['hobbies']) < 2:
        return None
    else:
        return students[0]['hobbies'][1]['hobbyAge']