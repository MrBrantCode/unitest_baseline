"""
QUESTION:
Implement a function `school_election_eligibility` that determines a user's eligibility to vote in a school election based on their age and grade level. The function should take two parameters: `age` (an integer representing the user's age) and `is_student` and `grade_level` (booleans representing whether the user is a student and integer representing the user's grade level). The function should return a string indicating whether the user is eligible to vote or not. 

Restrictions: The function should check the user's eligibility based on the following conditions:
- Teachers are not eligible to vote in the school election.
- Students in grade 12 who are 18 years or older are eligible to vote.
- Students in grade 12 who are younger than 18 years old are not eligible to vote.
- Students in grades 9 to 11 are not eligible to vote in the school election.
- Students in grades 6 to 8 are not eligible to vote, but can participate in future elections.
- Students in grades 1 to 5 are not eligible to vote.
"""

def school_election_eligibility(age, is_student, grade_level):
    """
    This function determines a user's eligibility to vote in a school election based on their age and grade level.

    Parameters:
    age (int): The user's age
    is_student (bool): Whether the user is a student
    grade_level (int): The user's grade level

    Returns:
    str: A string indicating whether the user is eligible to vote or not
    """
    if not is_student:
        return "Teachers are not eligible to vote in the school election."
    elif grade_level == 12 and age >= 18:
        return "Congratulations! You are eligible to vote in the school election."
    elif grade_level == 12 and age < 18:
        return "Sorry, you are not old enough to vote in the school election."
    elif grade_level >= 9 and grade_level <= 11:
        return "Students in grades 9 to 11 are not eligible to vote in the school election."
    elif grade_level >= 6 and grade_level <= 8:
        return "Students in grades 6 to 8 are not eligible to vote, but keep an eye out for future elections."
    elif grade_level >= 1 and grade_level <= 5:
        return "Sorry, voting is only open to students in grades 6 to 12."
    else:
        return "Invalid grade level."