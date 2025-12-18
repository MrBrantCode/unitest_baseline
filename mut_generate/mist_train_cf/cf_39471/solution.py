"""
QUESTION:
Write a function `process_registration(system, registered, new_course)` that processes a course registration system based on the given rules. 

The function takes three parameters: `system`, a string representing the course registration system where each character represents a course code and the position indicates the priority; `registered`, a string representing the courses the student is already registered for; and `new_course`, a character representing the new course the student wants to register for.

The function returns a string representing the updated list of registered courses after processing the new course registration request. If the new course has a higher priority than the ones already registered, it replaces the lower priority course. If it has the same priority as the ones already registered, it is added to the list of registered courses.

Input strings will only contain uppercase letters and hyphens ("-"), and the length of the `system` string will be the same as the length of the `registered` string.
"""

def entrance(system, registered, new_course):
    updated_registered = list(registered)
    for i in range(len(system)):
        if system[i] == new_course:
            updated_registered[i] = new_course
        elif system[i] == '-' and updated_registered[i] == '-':
            updated_registered[i] = new_course
    return ''.join(updated_registered)